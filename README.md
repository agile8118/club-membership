# Club Membership Project

#### Installed packages for Python:

Install all of them using pip:

- Flask
- bcrypt
- PyJWT

#### How to run the app:

After pip installing the packages above, run `python app.py` from the working directory.

#### How to push your changes:

1. git pull origin main
2. git checkout -b \<branch-name>
3. git add .
4. git commit -m "Your commit message"
5. git push origin \<branch-name>

#### Folder structure:

We're going to have all our routes in app.py file. For each feature of our app, we add a new controller file in the controllers file, and put all the functionality of that there.
For example, for the authentication feature, we have a file called authentication.py that contains the logic for both logging in and registration. Then this file is imported in the app.py file and its functions are called for each corresponding route.

In the client folder, we have our react code. This folder produces a huge JavaScript file which is then put in the static folder.

For the sake of simplicity, we won't use a full-fledged database like PostgreSQL or MongoDB, instead we try to simulate a database ourselves. For that we'll save all our data in the data folder as JSON data. So now we just read and write to that folder for creating, reading, updating and deleting records.

#### Database:

We have a file called DB.py that we have to include in every file that we want to deal with the database.

So we first import:

```
import DB from DB
```

then initialize:

```
DB = DB()
```

and now we have to run this so that the DB object will read from the data folder and put all the data to the memory (so we'll have all the data on the DB object):

```
DB.update()
```

we can now easily do CRUD (create, read, update and delete) operations:

```
# the name of first user
DB.users[0]["name"]

# finds a user with a specific phone number
for user in DB.users:
    if user["phone"] == phone:
      print(user)

# Updates a record
DB.users[0]["name"] = "John Doe"
```

**IMPORTANT!** Every time we change something from the DB object, we have to run `DB.save()` to save all the data to the data folder.
