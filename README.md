# Role-Based User Authentication

## Overview
This project implements a role-based authentication system where users have different access levels based on their roles. Admins can view and manage all users, while regular users can only view their own details.

## Features
- User registration and authentication
- Role-based access control (Admin & Regular User)
- Secure password hashing
- Session management
- API endpoints for user management

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Kshitij0605/Role-Based-User-Authentication.git
   cd Role-Based-User-Authentication
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file and configure necessary environment variables.
4. Run database migrations:
   ```sh
   python manage.py migrate
   ```
5. Start the server:
   ```sh
   python manage.py runserver
   ```

## Usage
- **Register a user**: Users can sign up with their credentials.
- **Login**: Authenticate and obtain an access token.
- **Admin Access**: Admins can manage all users.
- **User Access**: Regular users can only view their own details.

## API Endpoints
| Method | Endpoint             | Description                        |
|--------|----------------------|------------------------------------|
| POST   | /api/register        | Register a new user               |
| POST   | /api/login           | Authenticate user                  |
| GET    | /api/users           | Get all users (Admin only)        |
| GET    | /api/users/<id>      | Get user details (Self or Admin)  |

## Technologies Used
- Python
- Django / Flask (Specify the framework used)
- SQLite / PostgreSQL (Specify the database used)
- JWT for authentication

## Security Measures
- Password hashing using bcrypt or Django's built-in security features
- Role-based access control (RBAC)
- Secure API authentication with JWT

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

## Contact
For any queries or issues, feel free to open an issue in the repository.

