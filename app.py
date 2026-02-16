from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from models import db
from routes import auth_routes

app = Flask(__name__)
CORS(app)

# JWT Secret Key (MUST MATCH sa auth.py)
app.config["SECRET_KEY"] = "super-secret-jwt-key-very-long-123456789"


# SQLite database config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#  Initialize extensions
db.init_app(app)
bcrypt = Bcrypt(app)

# Home route
@app.route("/")
def home():
    return {"message": "JWT Auth System Running"}

# Create database tables
with app.app_context():
    db.create_all()

# Register auth routes
app.register_blueprint(auth_routes)

if __name__ == "__main__":
    app.run(debug=True)
