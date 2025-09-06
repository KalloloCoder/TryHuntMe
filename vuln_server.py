#!/usr/bin/env python3
"""
Simple vulnerable server for TryHuntMe (local only)
Endpoints:
 - /            -> welcome
 - /xss         -> reflects query param (XSS demo)
 - /login       -> naive SQLi demo (simulated)
 - /cmd         -> simulated command injection (CRITICAL: only simulation)
 - /upload      -> allows file upload into ./uploads (for testing)
"""
import sys
import os
from flask import Flask, request, render_template_string, redirect, url_for, send_from_directory

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template_string("""
    <h1>TryHuntMe - Local Vulnerable Lab</h1>
    <p>Endpoints:</p>
    <ul>
      <li><a href="/xss?name=demo">/xss?name=...</a> (reflected XSS)</li>
      <li><a href="/login">/login</a> (simple login form — watch for SQLi)</li>
      <li><a href="/cmd?cmd=whoami">/cmd?cmd=...</a> (simulated command exec)</li>
      <li><a href="/upload">/upload</a> (simple file upload)</li>
    </ul>
    """)
# Reflected XSS
@app.route("/xss")
def xss():
    name = request.args.get("name", "")
    # intentionally reflect unsanitized
    return f"<h2>Search result for: {name}</h2>"

# Simulated login (do NOT actually run SQL injection against real DB)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("username", "")
        pwd = request.form.get("password", "")
        # naive "check" that is intentionally insecure (string compare)
        if user == "admin" and pwd == "password":
            return "<h3>Welcome admin!</h3>"
        else:
            # show (simulated) query
            simulated_query = f"SELECT * FROM users WHERE username='{user}' AND password='{pwd}';"
            return f"<pre>Executed: {simulated_query}</pre><p>Login failed.</p>"
    return """
    <form method="post">
      Username: <input name="username"><br>
      Password: <input name="password"><br>
      <input type="submit" value="Login">
    </form>
    """

# Simulated command endpoint — DO NOT EXECUTE OS COMMANDS
@app.route("/cmd")
def cmd():
    cmd = request.args.get("cmd", "")
    # Danger: do NOT actually run commands; we simulate output
    fake_output = f"Simulated execution of: {cmd}\nOutput:\nthis_is_simulated_output"
    return f"<pre>{fake_output}</pre>"

# File upload demo
@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        f = request.files.get("file")
        if f:
            path = os.path.join(UPLOAD_FOLDER, f.filename)
            f.save(path)
            return f"Saved to {path}"
    return """
    <h3>Upload a file (saved to uploads/)</h3>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file"><input type="submit" value="Upload">
    </form>
    """

# serve uploaded files for convenience (local)
@app.route("/uploads/<path:filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except:
            pass
    app.run(host="127.0.0.1", port=port, debug=False)
