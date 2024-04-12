# This file adds some seed data to the database. Wipes everything clean.

import json
import os
# from DB import DB

# DB = DB()

# All passwords are 123
users = [
    {
        "id": 1,
        "name": "Joe",
        "phone": "4161",
        "email": "joe@gmail.com",
        "address": "123 Some Street",
        "password": "JDJiJDEyJDViZlowLkQxRXVwQ2pQUUhqbE5WRk8xM0RJc0hSQmFRbVdyM2dTODVOL1NSblFTTkNianFT",
        "role": "treasurer"
    },
    {
        "id": 2,
        "name": "Adam",
        "phone": "4162",
        "email": "adam@gmail.com",
        "address": "234 Some Street",
        "password": "JDJiJDEyJDViZlowLkQxRXVwQ2pQUUhqbE5WRk8xM0RJc0hSQmFRbVdyM2dTODVOL1NSblFTTkNianFT",
        "role": "coach"
    },
    {
        "id": 3,
        "name": "Victoria Anderson",
        "phone": "4163",
        "email": "victoria@gmail.com",
        "address": "543 Other Street",
        "password": "JDJiJDEyJDViZlowLkQxRXVwQ2pQUUhqbE5WRk8xM0RJc0hSQmFRbVdyM2dTODVOL1NSblFTTkNianFT",
        "role": "coach"
    },
    {
        "id": 4,
        "name": "Jane Miller",
        "phone": "4164",
        "email": "jane@gmail.com",
        "address": "324 Vic Street",
        "password": "JDJiJDEyJDViZlowLkQxRXVwQ2pQUUhqbE5WRk8xM0RJc0hSQmFRbVdyM2dTODVOL1NSblFTTkNianFT",
        "role": "member"
    },
    {
        "id": 5,
        "name": "Drake Clark",
        "phone": "4165",
        "email": "drake@gmail.com",
        "address": "431 Gerrard Street",
        "password": "JDJiJDEyJDViZlowLkQxRXVwQ2pQUUhqbE5WRk8xM0RJc0hSQmFRbVdyM2dTODVOL1NSblFTTkNianFT",
        "role": "member"
    }
]


practices = [
    {
        "id": 1,
        "date": "2024-04-10 17:00",
        "coach_id": 2,
        "price": 40,
        "members": [{"member_id": 4, "paid": False}, {"member_id": 5, "paid": False}]
    },
    {
        "id": 2,
        "date": "2024-04-12 17:00",
        "coach_id": 3,
        "price": 45,
        "members": [{"member_id": 4, "paid": False}, {"member_id": 5, "paid": True}]
    }

]

# Create the data folder if it doesn't exist

if not os.path.exists("./data"):
    os.makedirs("./data")

# create the data files
with open("./data/users", "w") as users_file:
    json.dump(users, users_file)

with open("./data/practices", "w") as practices_file:    
    json.dump(practices, practices_file)

with open("./data/sessions", "w") as sessions_file:
    json.dump([], sessions_file)


# Put the data to database
# DB.update()
# DB.users = users
# DB.practices = practices
# DB.save()