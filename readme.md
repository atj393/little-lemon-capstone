# Little Lemon Back-End Capstone Project

## API Endpoints

- `/api/menu/` - Menu management endpoint (GET, POST, PUT, DELETE)
- `/api/bookings/` - Booking management endpoint (GET, POST, PUT, DELETE)
- `/api/registration/` - User registration endpoint
- `/api/token/` - Obtain JWT token
- `/api/token/refresh/` - Refresh JWT token

## Setup Instructions

- Clone the repository and create a virtual environment.
- Install dependencies: `pip install -r requirements.txt`.
- Configure MySQL settings in `settings.py`.
- Run migrations: `python manage.py migrate`.
- Start the server: `python manage.py runserver`.
