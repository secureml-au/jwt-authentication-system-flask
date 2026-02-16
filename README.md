# 🔐 JWT Authentication System using Flask

A secure, production-ready token-based authentication backend built with Flask and JWT. This system implements industry-standard security practices for user registration, login validation, and protected API routes.

![JWT Authentication](https://img.shields.io/badge/JWT-Authentication-000000?style=for-the-badge&logo=JSON%20web%20tokens)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg?style=for-the-badge)

## 🌟 Features

- **🔒 Secure User Registration** - Password hashing with bcrypt
- **🎫 Token-Based Authentication** - JWT token generation and validation
- **🛡️ Protected API Routes** - Bearer token authorization
- **👤 User Login System** - Credential validation and session management
- **💾 Database Persistence** - SQLite with SQLAlchemy ORM
- **🚀 RESTful API** - Clean and standardized endpoints

## 🛠️ Tech Stack

### Backend
- **Python** - Core programming language
- **Flask** - Lightweight REST API framework

### Authentication & Security
- **JWT (JSON Web Token)** - Stateless token-based authentication
- **Flask-JWT / PyJWT** - Token encoding and decoding
- **bcrypt / Flask-Bcrypt** - Password hashing algorithm

### Database
- **SQLite** - Embedded database for user storage
- **SQLAlchemy** - Object-Relational Mapping (ORM)

## 📋 API Endpoints

| Method | Endpoint | Description | Authentication |
|--------|----------|-------------|----------------|
| POST | `/register` | Create new user account | ❌ Public |
| POST | `/login` | Authenticate and get JWT token | ❌ Public |
| GET | `/profile` | Get user profile information | ✅ Required |

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/ares-coding/jwt-authentication-flask.git
cd jwt-authentication-flask
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set environment variables**
```bash
export SECRET_KEY='your-secret-key-here'
export DATABASE_URL='sqlite:///users.db'
```

5. **Run the application**
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## 📝 Usage Examples

### 1. Register a New User

```bash
curl -X POST http://localhost:5000/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "SecurePass123!"
  }'
```

**Response:**
```json
{
  "message": "User registered successfully",
  "user_id": 1
}
```

### 2. Login and Get JWT Token

```bash
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "SecurePass123!"
  }'
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

### 3. Access Protected Route

```bash
curl -X GET http://localhost:5000/profile \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Response:**
```json
{
  "user_id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "created_at": "2024-02-16T10:30:00Z"
}
```

## 🔒 Security Features

- **Password Hashing**: All passwords are hashed using bcrypt with salt rounds
- **JWT Tokens**: Stateless authentication with configurable expiration
- **Bearer Token Authorization**: Industry-standard HTTP authentication
- **SQL Injection Protection**: SQLAlchemy ORM prevents SQL injection attacks
- **Input Validation**: Server-side validation for all user inputs

## 📂 Project Structure

```
jwt-authentication-flask/
├── app.py                 # Main application file
├── models.py              # Database models
├── auth.py                # Authentication logic
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── users.db              # SQLite database (generated)
```

## 🧪 Testing

Run the test suite:

```bash
python -m pytest tests/
```

## 📦 Dependencies

```
Flask==2.3.0
Flask-SQLAlchemy==3.0.0
Flask-Bcrypt==1.0.1
PyJWT==2.8.0
python-dotenv==1.0.0
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Au.dev**
- GitHub: [@ares-coding](https://github.com/ares-coding)

## Acknowledgments

- Flask documentation and community
- JWT.io for JWT standards
- bcrypt library maintainers

---

⭐ **Star this repository if you find it helpful!**
