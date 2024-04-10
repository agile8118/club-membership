from flask import (
    Flask,
    send_from_directory,
    jsonify,
    request,
)
from flask_cors import CORS
from DB import DB

DB = DB()

app = Flask(__name__)
CORS(app)


# Controllers
from controllers.authentication import Authentication
from controllers.practice import Practice


# Middleware to check if user is authenticated
@app.before_request
def check_authentication():
    non_protected_routes = ["/login", "/register", "/"]
    if request.path not in non_protected_routes and not request.path.startswith(
        "/static"
    ):
        auth_token = request.headers.get("Authorization")

        if not auth_token:
            return jsonify({"error": "Unauthorized"}), 401

        # Check if token is valid
        DB.update()
        for session in DB.sessions:
            if session["token"] == auth_token:
                request.user_id = session["user_id"]
                return

        return jsonify({"error": "Unauthorized"}), 401


# Middleware to serve the index.html file for different routes
@app.before_request
def send_index_file():
    if request.method == "GET" and request.path in ["/", "/login", "/register"]:
        return send_from_directory(app.static_folder, "index.html")


# Example of an accepted JSON body:
# {
#     "phone": "1234567890",
#     "password": "password",
# }
#
# Example of a response:
# {
#     "message": "Login successful",
#     "token": "some-token"
# }
#
# Token should be sent in the Authorization header for future requests
@app.route("/login", methods=["POST", "GET", "OPTIONS"])
def login():
    if request.method == "POST":
        return Authentication.login()


# Example of an accepted JSON body:
# {
#     "name": "John Doe",
#     "email": "john@company.com",
#     "address": "123 Some Street",
#     "phone": "1234567890",
#     "password": "password",
# }
#
# Example of a response:
# {
#     "message": "User registered successfully.",
#     "token": "some-token"
# }
#
# Token should be sent in the Authorization header for future requests
@app.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        return Authentication.register()


# This route will create a new practice session. ONLY a treasurer should
# be able to do this.
# Example of an accepted JSON body:
# {
#     "date": "2024-04-10 17:00:00",
#     "coach": "Adam",
# }
#
# Example of a response:
# {
#     "message": "Practice session successfully scheduled.",
# }
#
@app.route("/practice", methods=["POST"])
def create_class():
    if request.method == "POST":
        return Practice.create()


# Example of route that requires authentication
# The user_id is available in the request object as request.user_id
# This only happens if the we have a valid token in the Authorization header
# Check this function to see how it's done: check_authentication()
@app.route("/protected-test", methods=["GET"])
def pt():
    if request.method == "GET":
        return jsonify({"user": request.user_id})


if __name__ == "__main__":
    app.run(debug=True)
