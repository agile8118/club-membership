from flask import (
    Flask,
    send_from_directory,
    jsonify,
    request,
)
from DB import DB

DB = DB()

# Controllers
from controllers.authentication import Authentication


app = Flask(__name__)


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


@app.route("/")
def home():
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
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        return Authentication.login()
    if request.method == "GET":
        return send_from_directory(app.static_folder, "index.html")


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
