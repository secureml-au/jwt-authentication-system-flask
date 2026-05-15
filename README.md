# JWT Authentication System — Flask

> Secure, production-ready token-based authentication backend built with Flask and JWT.

![JWT](https://img.shields.io/badge/JWT-Authentication-000000?style=flat-square&logo=JSON%20web%20tokens)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=flat-square&logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg?style=flat-square)

---
<img width="1536" height="1024" alt="Image" src="https://github.com/user-attachments/assets/746220bf-1445-42c8-8d6a-65975048b7b5" />

## Overview
A minimal yet robust authentication system implementing industry-standard security practices — bcrypt password hashing, stateless JWT sessions, and protected API routes via Bearer token authorization.

---

## Features

- Secure user registration with bcrypt password hashing
- JWT token generation, signing, and validation
- Protected API routes via Bearer token authorization
- Credential validation and session management
- SQLite persistence via SQLAlchemy ORM
- Clean RESTful API design

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.8+ |
| Framework | Flask |
| Auth | PyJWT, Flask-Bcrypt |
| Database | SQLite + SQLAlchemy ORM |

---

## API Endpoints

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| POST | `/register` | Create new user account | No |
| POST | `/login` | Authenticate and receive JWT | No |
| GET | `/profile` | Retrieve user profile | Yes |

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/ares-coding/jwt-authentication-flask.git
cd jwt-authentication-flask

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export SECRET_KEY='your-secret-key-here'
export DATABASE_URL='sqlite:///users.db'

# Run the application
python app.py
```

Server runs at `http://localhost:5000`

---

## Usage

### Register

```bash
curl -X POST http://localhost:5000/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "SecurePass123!"
  }'
```

```json
{
  "message": "User registered successfully",
  "user_id": 1
}
```

### Login

```bash
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "SecurePass123!"
  }'
```

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

### Access Protected Route

```bash
curl -X GET http://localhost:5000/profile \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

```json
{
  "user_id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "created_at": "2024-02-16T10:30:00Z"
}
```

---

## Security

- Passwords hashed via bcrypt with salt rounds
- Stateless JWT with configurable expiration
- Bearer token authorization (RFC 6750)
- SQL injection prevention via SQLAlchemy ORM
- Server-side input validation on all endpoints

---

## Project Structure

```
jwt-authentication-flask/
├── app.py              # Application entry point
├── models.py           # Database models
├── auth.py             # Authentication logic
├── config.py           # Configuration settings
├── requirements.txt    # Dependencies
├── README.md
└── users.db            # SQLite database (auto-generated)
```

---

## Dependencies

```
Flask==2.3.0
Flask-SQLAlchemy==3.0.0
Flask-Bcrypt==1.0.1
PyJWT==2.8.0
python-dotenv==1.0.0
```

---

## Testing

```bash
python -m pytest tests/
```

---

## Contributing

1. Fork the repository
2. Create a feature branch — `git checkout -b feature/your-feature`
3. Commit your changes — `git commit -m 'Add your feature'`
4. Push the branch — `git push origin feature/your-feature`
5. Open a Pull Request

---

## License

Licensed under the [Apache License 2.0](LICENSE).

---

**Author:** Au.dev — [@ares-coding](https://github.com/ares-coding)
