from flask import Blueprint, request, jsonify
from models import db, User
from flask_bcrypt import Bcrypt
from auth import generate_token, token_required

auth_routes = Blueprint("auth_routes", __name__)
bcrypt = Bcrypt()

@auth_routes.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Username and password required"}), 400

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"message": "User already exists"}), 409

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


@auth_routes.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Username and password required"}), 400

    user = User.query.filter_by(username=username).first()

    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({"message": "Invalid username or password"}), 401

    token = generate_token(user.id)

    return jsonify({
        "message": "Login successful",
        "token": token
    }), 200


@auth_routes.route("/profile", methods=["GET"])
@token_required
def profile(current_user):
    return jsonify({
        "id": current_user.id,
        "username": current_user.username
    })
