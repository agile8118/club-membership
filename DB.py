import json


class DB:
    def __init__(self):
        self.users_path = "./data/users"
        self.sessions_path = "./data/sessions"
        self.practices_path = "./data/practices"

        with open(self.users_path, "r") as users_file:
            self.users = json.load(users_file)

        with open(self.sessions_path, "r") as sessions_file:
            self.sessions = json.load(sessions_file)

        with open(self.practices_path, "r") as practices_file:
            self.practices = json.load(practices_file)


    def update(self):
        with open(self.users_path, "r") as users_file:
            self.users = json.load(users_file)

        with open(self.sessions_path, "r") as sessions_file:
            self.sessions = json.load(sessions_file)

        with open(self.practices_path, "r") as practices_file:
            self.practices = json.load(practices_file)


    def save(self):
        with open(self.users_path, "w") as users_file:
            json.dump(self.users, users_file)

        with open(self.sessions_path, "w") as sessions_file:
            json.dump(self.sessions, sessions_file)


        with open(self.practices_path, "w") as practices_file:
            json.dump(self.practices, practices_file)
