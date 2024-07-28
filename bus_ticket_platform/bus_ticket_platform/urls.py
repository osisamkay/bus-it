from django.contrib import admin
from django.urls import path, include
from ninja_extra import NinjaExtraAPI
from api.auth.endpoints import router as auth_router
from api.all_route.endpoints import router as search_routes_router
from api.book_tickets.endpoints import router as book_tickets_router
from api.manage_bookings.endpoints import router as manage_bookings_router
from api.explore_deals.endpoints import router as explore_deals_router
from api.customer_support.endpoints import router as customer_support_router
from api.account_settings.endpoints import router as account_settings_router
from api.vehicles.endpoints import router as vehicles_router

api = NinjaExtraAPI()


api.add_router("/auth/", auth_router)
api.add_router("/routes/", search_routes_router)
api.add_router("/book_tickets/", book_tickets_router)
api.add_router("/manage_bookings/", manage_bookings_router)
api.add_router("/explore_deals/", explore_deals_router)
api.add_router("/customer_support/", customer_support_router)
api.add_router("/account_settings/", account_settings_router)
api.add_router("/vehicles/", vehicles_router)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    path('api/password_reset/',
         include('django_rest_passwordreset.urls', namespace='password_reset')),
]
