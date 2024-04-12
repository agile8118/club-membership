from flask import Flask, request, jsonify
from DB import DB
from datetime import datetime 

DB = DB()


class Practice:
    @staticmethod
    # Create the practice session here and add it to the database
    def create():

        coach = request.json.get("coach")
        date = request.json.get("date")

        practice_session = {
            "coach": coach,
            "date": date
        }

        DB.update()
        DB.practices.append(practice_session)
        DB.save()

        return jsonify({"message": "Practice Session Created"})
    
    @staticmethod
    # Schedule a user for an upcoming practice class
    def signup():
        
        id = request.json.get("id")
        coach = request.json.get("coach")
        date = request.json.get("date")

        scheduled_classes = {
            "id": id,
            "coach": coach,
            "date": date
        }

        DB.update()
        DB.practices.append(scheduled_classes)
        DB.save()

        return jsonify({"message": "Practice Session Scheduled"})
    
    @staticmethod
    # User can view upcoming classes
    def get_practices():
        DB.update()
        return jsonify(DB.practices)

        