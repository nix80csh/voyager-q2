# signup_app.py
from flask import Flask, request, jsonify
import json
from db_handler import read_users, write_users, initialize_db

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    print("Received data:", json.dumps(data, indent=2, ensure_ascii=False))
    
    if not data or 'name' not in data:
        return jsonify({'error': 'Missing name or email'}), 400

    users = read_users()
    users.append({'name': data['name'], 'email': data.get('email', '')})
    write_users(users)
    return jsonify({'status': 'ok!'})

if __name__ == '__main__':
    initialize_db()
    app.run(host='0.0.0.0', port=5002, debug=True)
