from flask import request, jsonify
import bcrypt
import random
import base64
from DB import DB

DB = DB()


class Authentication:
    @staticmethod
    def login():
        # get username and password from request body as JSON
        phone = request.json.get("phone")
        password = request.json.get("password")

        DB.update()

        # perform authentication here
        for user in DB.users:
            if user["phone"] == phone:
                hashed_password_base64 = user["password"]
                hashed_password = base64.b64decode(
                    hashed_password_base64.encode("utf-8")
                )

                if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
                    # Generate a random token
                    token = str(random.randint(0, 10000000000))

                    # remove the previous session token if it exists
                    for session in DB.sessions:
                        if session["user_id"] == user.get("id"):
                            DB.sessions.remove(session)

                    DB.sessions.append({"token": token, "user_id": user.get("id")})
                    DB.save()

                    return jsonify({"message": "Login successful", "token": token})

        # return error message if authentication fails
        return jsonify({"error": "Invalid phone or password"})

    @staticmethod
    def register():
        name = request.json.get("name")
        phone = request.json.get("phone")
        email = request.json.get("email")
        address = request.json.get("address")
        password = request.json.get("password")

        # hash the provided password
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        # convert the hashed password to base64 to be able to save to a file as JSON
        hashed_password_base64 = base64.b64encode(hashed_password).decode("utf-8")

        # check if phone and email not taken
        for user in DB.users:
            if user["phone"] == phone:
                return jsonify({"error": "Phone number already taken"})
            if user["email"] == email:
                return jsonify({"error": "Email already taken"})

        # add user to DB
        user = {
            "id": len(DB.users) + 1,
            "name": name,
            "phone": phone,
            "email": email,
            "address": address,
            "password": hashed_password_base64,
        }
        print(hashed_password_base64)
        DB.users.append(user)

        # Generate a random token
        token = str(random.randint(0, 10000000000))
        DB.sessions.append({"token": token, "user_id": user.get("id")})

        # save DB
        DB.save()

        return jsonify({"message": "User registered successfully.", "token": token})
