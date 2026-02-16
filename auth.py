import jwt
from datetime import datetime, timedelta
from functools import wraps
from flask import request, jsonify
from models import User

SECRET_KEY = "super-secret-jwt-key-very-long-123456789"


def generate_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(hours=2)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return jsonify({"message": "Token is missing"}), 401

        try:
            token = auth_header.split(" ")[1]  # remove Bearer
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = User.query.get(data["user_id"])
        except:
            return jsonify({"message": "Invalid or expired token"}), 401

        return f(current_user, *args, **kwargs)

    return decorated
