from flask import (
    Flask,
    send_from_directory,
    jsonify,
    render_template,
    request,
    redirect,
    url_for,
)

# Controllers
from controllers.authentication import Authentication


app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True)
