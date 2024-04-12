from flask import Flask, request, jsonify
from DB import DB
from datetime import datetime 

DB = DB()


class Practice:
    @staticmethod
    # Create a practice session here and add it to the database
    def create():
        DB.update()
        coach = request.json.get("coach")
        name = request.json.get("name")
        date = request.json.get("date")
        time = request.json.get("time")
        price = request.json.get("price")

        practice_session =  {
            "id": len(DB.practices) + 1,
            "coach_id": int(coach),
            "name": name,
            "date": date,
            "time": time,
            "price": int(price),
            "coach_attended": False,
            "members": []
        }

        DB.practices.append(practice_session)
        DB.save()

        return jsonify({"message": "Practice session created successfully."})
    
    @staticmethod
    # Schedule a user for an upcoming practice class
    def signup():
        DB.update()
        session_id = request.json.get("session_id")
        # find the practice session with the same id as the session_id
        for practice in DB.practices:
            if practice["id"] == session_id:
                # check if the user is already signed up
                for member in practice["members"]:
                    if member["member_id"] == request.user_id:
                        return jsonify({"message": "You are already signed up for this practice session."})
                   
                practice["members"].append({"member_id": request.user_id, "paid": False})
                DB.save()
                return jsonify({"message": "Successfully signup for the practice session."})
                
        return jsonify({"message": "Practice session not found."}), 404
                
    
    @staticmethod
    def cancel_signup():
        DB.update()
        session_id = request.json.get("session_id")
        # find the practice session with the same id as the session_id
        for practice in DB.practices:
            if practice["id"] == session_id:
                # check if the user is already signed up
                for member in practice["members"]:
                    if member["member_id"] == request.user_id:
                        practice["members"].remove(member)
                        DB.save()
                        return jsonify({"message": "You have successfully cancelled your signup for the practice session."})
                    
                return jsonify({"message": "You are not signed up for this practice session."}), 401
                
        return jsonify({"message": "Practice session not found."}), 404

    @staticmethod
    def practice_pay():
        DB.update()
        session_id = request.json.get("session_id")
        # find the practice session with the same id as the session_id
        for practice in DB.practices:
            if practice["id"] == session_id:
                # check if the user is already signed up
                for member in practice["members"]:
                    if member["member_id"] == request.user_id:
                        member["paid"] = True
                        DB.save()
                        return jsonify({"message": "You have successfully paid for the practice session."})
                    
                return jsonify({"message": "You are not signed up for this practice session."}), 401
                
        return jsonify({"message": "Practice session not found."}), 404

    
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

        