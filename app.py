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

# Middleware to serve the index.html file for different routes
@app.before_request
def send_index_file():
    if request.method == "GET" and request.path in ["/", "/login", "/register", "/practice-classes", "/practice-create"]:
        return send_from_directory(app.static_folder, "index.html")


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


@app.route("/logout", methods=["DELETE"])
def logout():
    if request.method == "DELETE":
        return Authentication.logout()


# Example of route that requires authentication
# The user_id is available in the request object as request.user_id
# This only happens if the we have a valid token in the Authorization header
# Check this function to see how it's done: check_authentication()
@app.route("/is-logged-in", methods=["POST"])
def is_logged_in():
    if request.method == "POST":
        # find the user in the DB and return the role
        for user in DB.users:
            if user["id"] == request.user_id:
                return jsonify({"user_id": request.user_id, "role": user["role"]})
        

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
@app.route("/practice-create", methods=["POST"])
def create_class():
    if request.method == "POST":
        return Practice.create()

# This route will add a user to an upcoming created practice session. A member 
# must be signed in to be able to do this. The user_id should be read from request.user_id.
# Example of an accepted JSON body:
# {
#     "practice_id": "23"
# }
#
# Example of a response:
# {
#     "message": "You have been scheduled for this class.",
# }
@app.route("/practice-signup", methods=["POST"])
def sign_up_class():
    if request.method == "POST":
        return Practice.signup()

@app.route("/practices", methods=["GET"])
def get_practices():
    if request.method == "GET":
        return Practice.get_practices()


if __name__ == "__main__":
    app.run(debug=True)
