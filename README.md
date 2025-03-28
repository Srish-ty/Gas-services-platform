# Gas Services Platform

## Overview
Gas Services Platform is a Django-based web application designed to streamline consumer services for gas utilities. It enables customers to submit service requests, track their status, and manage their account information efficiently. Additionally, the platform provides customer support representatives with tools to handle and resolve service requests effectively.

## Features

### For Customers
- **Service Request Submission**: Customers can submit service requests online, specifying the type of service needed and attaching relevant files if required.
- **Request Tracking**: Users can track the status of their service requests, including submission and resolution timestamps.
- **Account Management**: Customers can view and manage their account details and request history.

### For Customer Support Representatives
- **Request Management**: View, filter, and update service requests from customers.
- **Customer Support**: Communicate with customers and provide updates on their requests.
- **Service Resolution**: Mark requests as resolved and add resolution notes.

## Tech Stack
- **Backend**: Django (Python)
- **Database**: SQLite
- **Frontend**: Django templates
- **Deployment**: Render

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Srish-ty/Gas-services-platform.git
   cd Gas-services-platform
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```sh
   python manage.py migrate
   ```

5. Run the development server:
   ```sh
   python manage.py runserver
   ```

## Deployment
To deploy on Render, ensure you have the following environment variables set up:
https://gas-services-platform.onrender.com/

Then push your code to GitHub and connect the repository to Render for automatic deployment.

## Bonus: Django Project Structure
```
Gas-services-platform/
│-- manage.py
│-- requirements.txt
│-- .env (environment variables - not committed)
│
├── gas_services/  # Main Django application
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── services/  # App handling service requests
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── admin.py
│
├── users/  # App handling user authentication & accounts
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── admin.py
```

## Contributing
Pull requests are welcome! Please follow the coding standards and submit any issues or suggestions.

## License
MIT License

