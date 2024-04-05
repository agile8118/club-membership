from flask import request, jsonify
from DB import DB

DB = DB()

class Users:
  @staticmethod
  def getUsers():
    DB.update()

    return jsonify(DB.users)
