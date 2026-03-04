from flask import Flask, request
import sqlite3
import subprocess
import hashlib
import os

app = Flask(__name__)

# 🔴 VULNERABILITY 1: Hardcoded secret credentials
SECRET_KEY = "supersecret123"
DB_PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"

# 🔴 VULNERABILITY 2: SQL Injection
@app.route("/user")
def get_user():
    username = request.args.get("username")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # DANGER: user input directly in SQL query
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return str(cursor.fetchall())

# 🔴 VULNERABILITY 3: Command Injection
@app.route("/ping")
def ping():
    host = request.args.get("host")
    # DANGER: user input passed directly to shell
    result = subprocess.run("ping -c 1 " + host, shell=True, capture_output=True)
    return result.stdout.decode()

# 🔴 VULNERABILITY 4: Weak hashing algorithm (MD5)
@app.route("/login", methods=["POST"])
def login():
    password = request.form.get("password")
    # DANGER: MD5 is cryptographically broken
    hashed = hashlib.md5(password.encode()).hexdigest()
    return {"hash": hashed}

# 🔴 VULNERABILITY 5: Path Traversal
@app.route("/file")
def read_file():
    filename = request.args.get("name")
    # DANGER: attacker can read any file on the server
    with open("/var/data/" + filename, "r") as f:
        return f.read()

# 🔴 VULNERABILITY 6: Debug mode ON in production
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
