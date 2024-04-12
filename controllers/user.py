from flask import Flask, request, jsonify
from DB import DB
from datetime import datetime 

DB = DB()


class User:
  @staticmethod
  def get_user_info():
    DB.update()
    # find the user object with the same id as the user_id
    for user in DB.users:
        if user["id"] == request.user_id:
            return jsonify(user)
    

  @staticmethod
  def get_coaches():
    DB.update()
    coaches = []
    for user in DB.users:
        if user["role"] == "coach":
            coaches.append(user)
    return jsonify(coaches)


