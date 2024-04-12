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
        # loop through the practices and add the coach name
        for practice in DB.practices:
            # remove all members that are not user_id, have it as dictionary
            practice["members"] = [member for member in practice["members"] if member["member_id"] == request.user_id]
            if practice["members"]:
              practice["member_attend"] = True
              practice["member_paid"] = practice["members"][0]["paid"]
              del practice["members"]
            # find the user with the same id as the coach_id
            for user in DB.users:
                if user["id"] == practice["coach_id"]:
                    practice["coach"] = user["name"]
                    break
                
                
        return jsonify(DB.practices)

        