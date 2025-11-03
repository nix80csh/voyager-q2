
import json
import os

DB_FILE = '/app/data/db.json'

def initialize_db():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False)

def read_users():
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_users(users):
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False)
