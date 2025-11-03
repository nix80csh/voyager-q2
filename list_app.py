# list_app.py
from flask import Flask, jsonify
from db_handler import read_users, initialize_db

app = Flask(__name__)

@app.route('/users')
def users():
    users = read_users()
    return jsonify(users), 200

if __name__ == '__main__':
    initialize_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
