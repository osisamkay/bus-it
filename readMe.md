# Bus Ticket Platform

## Overview

Bus Ticket Platform is a web application designed to streamline the process of booking and managing bus tickets. The platform offers various features, including searching for routes, booking tickets, managing bookings, exploring deals, and customer support.

## Features

- User Authentication and Authorization
- Route Search and Booking
- Booking Management
- Explore Deals
- Customer Support
- Account Settings

## Technologies Used

- Django 5.0.2
- Django Ninja
- Django REST Framework
- SimpleJWT for Authentication
- Allauth for Social Authentication
- Celery for Asynchronous Task Management

## Setup and Installation

### Prerequisites

- Python 3.8 or later
- Django 5.0.2
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/your-username/bus_ticket_platform.git
   cd bus_ticket_platform

   ```

2. Create and activate a virtual environment:

   ```sh
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`

   ```

3. Install the required dependencies:

   ```sh
   pip install -r requirements.txt

   ```

4. Set up environment variables:

   - EMAIL_HOST=smtp.example.com
   - EMAIL_PORT=587
   - EMAIL_USE_TLS=True
   - EMAIL_HOST_USER=your-email@example.com
   - EMAIL_HOST_PASSWORD=your-email-password
   - DEFAULT_FROM_EMAIL=your-email@example.com
   - CELERY_BROKER_URL=redis://localhost:6379/0
   - CELERY_RESULT_BACKEND=redis://localhost:6379/0

5. Run database migrations:

   ```sh
   python manage.py migrate


   ```

   Usage
   Visit http://127.0.0.1:8000/admin/ to access the admin panel.

Visit http://127.0.0.1:8000/api/ to access the API endpoints.

<!-- API Endpoints
/api/auth/login/ - Login endpoint
/api/auth/token/refresh/ - Token refresh endpoint
/api/search_routes/ - Search routes endpoint
/api/book_tickets/ - Book tickets endpoint
/api/manage_bookings/ - Manage bookings endpoint
/api/explore_deals/ - Explore deals endpoint
/api/customer_support/ - Customer support endpoint
/api/account_settings/ - Account settings endpoint
Example Requests
Login
http
Copy code
POST /api/auth/login/
Content-Type: application/json -->

<!-- {
  "email": "user@example.com",
  "password": "password123"
}
Search Routes
http
Copy code
GET /api/search_routes/?origin=CityA&destination=CityB&date=2023-01-01
Book Ticket
http
Copy code
POST /api/book_tickets/
Content-Type: application/json

{
  "route_id": 1,
  "passenger_name": "John Doe",
  "passenger_email": "john@example.com"
} -->
<!-- Manage Booking
http
Copy code
GET /api/manage_bookings/?booking_id=123
Explore Deals
http
Copy code
GET /api/explore_deals/
Customer Support
http
Copy code
POST /api/customer_support/
Content-Type: application/json -->

<!-- {
  "subject": "Issue with Booking",
  "message": "I have an issue with my booking."
}
Account Settings
http
Copy code
GET /api/account_settings/
Contributing
Contributions are welcome! Please create an issue or submit a pull request.

License
This project is licensed under the MIT License.

markdown
Copy code -->

<!-- ## Authors

- Your Name - [your-github-username](https://github.com/your-github-username) -->
