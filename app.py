from flask import Flask, render_template, request, redirect, url_for, session
import pymysql
import os
from urllib.parse import urlparse

app = Flask(__name__)

# 🔐 Secret key from environment
app.secret_key = os.getenv("SECRET_KEY", "dev-secret")

# 🔌 Database connection (Render + Railway compatible)
def get_db():
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise RuntimeError(
            "DATABASE_URL is not set. Add it in Render Environment Variables."
        )

    url = urlparse(database_url)

    return pymysql.connect(
        host=url.hostname,
        user=url.username,
        password=url.password,
        database=url.path[1:],  # remove leading '/'
        port=url.port,
        cursorclass=pymysql.cursors.DictCursor,
        ssl={"ssl": {}}  # required for Railway MySQL
    )

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        try:
            conn = get_db()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                (username, email, password)
            )
            conn.commit()
            conn.close()
            return redirect(url_for("login"))
        except Exception as e:
            return f"Error: {e}"

    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM users WHERE email=%s AND password=%s",
            (email, password)
        )
        user = cur.fetchone()
        conn.close()

        if user:
            session["user"] = user["username"]
            return redirect(url_for("home"))
        else:
            return "Invalid credentials"

    return render_template("login.html")

@app.route("/home")
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("home.html", user=session["user"])

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# 🚀 Local only (ignored by Render)
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 5000)),
        debug=False
    )
