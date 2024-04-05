from flask import (
    Flask,
    send_from_directory,
    jsonify,
    render_template,
    request,
    redirect,
    url_for,
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


@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        return Authentication.login()


@app.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        return Authentication.register()


@app.route("/protected-test", methods=["GET"])
def pt():
    if request.method == "GET":
        return jsonify({"user": request.user_id})


if __name__ == "__main__":
    app.run(debug=True)
