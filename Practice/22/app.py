from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# データベースのパスを調整
DATABASE = 'users.sqlite'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50) NOT NULL,
            age INTEGER
        )
    """)
    conn.commit()
    conn.close()

def insert_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    if count == 0:
        users = [
            ('Alice', 20),
            ('Bob', None)
        ]
        cursor.executemany("""
            INSERT INTO users (name, age) VALUES(?, ?)
        """, users)
        conn.commit()

    conn.close()

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    user_list = []
    for user in users:
        user_list.append(dict(user))
    return jsonify({'users': user_list})

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (id,)).fetchone()
    conn.close()
    if user:
        return jsonify({'user': dict(user)})
    return jsonify({'message': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')

    if not name:
        return jsonify({'message': 'Name is required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users (name, age) VALUES(?, ?)
    """, (name, age))
    conn.commit()
    new_user_id = cursor.lastrowid
    conn.close()

    conn = get_db_connection()
    new_user = conn.execute('SELECT * FROM users WHERE id = ?', (new_user_id,)).fetchone()
    conn.close()
    return jsonify({'user': dict(new_user)}), 201

if __name__ == "__main__":
    create_db()
    insert_data()
    app.run(host='0.0.0.0', port=5000, debug=True)
