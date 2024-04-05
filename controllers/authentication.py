from flask import request, jsonify
import bcrypt
from DB import DB

DB = DB()


class Authentication:
    @staticmethod
    def login():
        # get username and password from request body as JSON
        phone = request.json.get("phone")
        password = request.json.get("password")

        # perform authentication here
        for user in DB.users:
            if user["phone"] == phone:
                if bcrypt.checkpw(password.encode("utf-8"), user["password"]):
                    return jsonify({"message": "Login successful"})

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

        print(DB.users[0]["name"])

        # check if phone and email not taken
        for user in DB.users:
            if user["phone"] == phone:
                return jsonify({"error": "Phone number already taken"})
            if user["email"] == email:
                return jsonify({"error": "Email already taken"})

        # add user to DB
        DB.users.append(
            {
                "id": len(DB.users) + 1,
                "name": name,
                "phone": phone,
                "email": email,
                "address": address,
                "password": hashed_password,
            }
        )

        # save DB
        DB.save()

        return "HEY"
