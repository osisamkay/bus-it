from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Route
from uuid import uuid4


class RouteTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.route = Route.objects.create(
            id=uuid4(),
            name='Test Route',
            description='A test route',
            start_point='Point A',
            end_point='Point B',
            distance=100.0,
            duration=60,
            price=10.0,
            trip_type='one_way_trip',
            user=self.user
        )

    def test_create_route(self):
        payload = {
            "name": "New Route",
            "description": "A new route description",
            "start_point": "New Point A",
            "end_point": "New Point B",
            "distance": 200.0,
            "duration": 120,
            "price": 20.0,
            "trip_type": "one_way_trip"
        }
        response = self.client.post(
            '/api/all_route/create_route', payload, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], payload['name'])

    def test_get_one_way_trips(self):
        response = self.client.get('/api/all_route/one_way_trips')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['total'], 1)
        self.assertEqual(response.data['routes'][0]['name'], self.route.name)

    def test_update_route(self):
        payload = {
            "name": "Updated Route",
            "description": "Updated description",
            "start_point": "Updated Point A",
            "end_point": "Updated Point B",
            "distance": 150.0,
            "duration": 90,
            "price": 15.0,
            "trip_type": "one_way_trip"
        }
        response = self.client.put(
            f'/api/all_route/route/{self.route.id}', payload, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], payload['name'])

    def test_delete_route(self):
        response = self.client.delete(f'/api/all_route/route/{self.route.id}')
        self.assertEqual(response.status_code, 204)

    def test_get_route_by_id(self):
        response = self.client.get(f'/api/all_route/route/{self.route.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], self.route.name)

    def test_get_round_trips(self):
        self.route.trip_type = 'round_trip'
        self.route.save()
        response = self.client.get('/api/all_route/round_trips')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['total'], 1)
        self.assertEqual(response.data['routes'][0]['name'], self.route.name)

    def test_search_routes(self):
        response = self.client.get('/api/all_route/search', {'query': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['total'], 1)
        self.assertEqual(response.data['routes'][0]['name'], self.route.name)

    def test_popular_routes(self):
        response = self.client.get('/api/all_route/popular_routes')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['total'], 1)
        self.assertEqual(response.data['routes'][0]['name'], self.route.name)
