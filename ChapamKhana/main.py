from flask import Flask, jsonify, request
from pymongo import MongoClient

app=Flask(__name__)

# dn_name='chapZoometo'
connection_Url='mongodb+srv://dhirajrajpp:root@cluster0.gphyqvp.mongodb.net/?retryWrites=true&w=majority'


def get_db():
    client = MongoClient(connection_Url)
    db= client.chapZometo
    return db

@app.route('/mongo')
def index():
    db = get_db()
    # Use the database connection to perform operations
    # For example, db.collection.find() or db.collection.insert_one()
    return 'Connected to MongoDB!'

@app.route('/')
def welcome():
    return 'Welcome to MongoDB, ChapZoometo'

@app.route('/users')
def create_user():
    # Retrieve user data from the request
    db=get_db()
    print("welcome")
    db.users.insert_one({ "id": 1, "name": "A", "Location": "Delhi"})
    print(db)


    return jsonify({'message': 'User created successfully'})

@app.route('/user')
def get_all_users():
    db=get_db()
    # Retrieve all users from the 'users' collection
    users = list(db.users.find())
    print(users)
    return jsonify({'message':'data get successfully'})


if __name__ == '__main__':
    app.run(debug=True)
