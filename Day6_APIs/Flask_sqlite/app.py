from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB = 'database.db'

#Create DB table
def init_db():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()  # call once at startup

#Helper: Fetch all as dicts
def to_dict(user_row):
    return {"id": user_row[0], "name": user_row[1], "email": user_row[2]}


#GET all users
@app.route('/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return jsonify([to_dict(u) for u in users])


# 🟢GET single user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    if user:
        return jsonify(to_dict(user))
    return jsonify({"error": "User not found"}), 404


#POST new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    name, email = data['name'], data['email']
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        new_id = cursor.lastrowid
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({"error": "Email already exists"}), 400
    conn.close()
    return jsonify({"id": new_id, "name": name, "email": email}), 201


#PUT update user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name, email = data['name'], data['email']
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id))
    conn.commit()
    conn.close()
    return jsonify({"id": user_id, "name": name, "email": email})


#DELETE user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "User deleted successfully"})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)