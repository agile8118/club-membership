from flask import request, jsonify
from DB import DB

DB = DB()


class Practice:
    @staticmethod
    # Create the practice session here and add it to the database
    def create():
        return jsonify({"message": "Feature coming soon!"})
    
    @staticmethod
    # Schedule a user for an upcoming practice class
    def signup():
        return jsonify({"message": "Feature coming soon!"})

