from flask import Flask, render_template, request, redirect, url_for, session
import pymysql

app = Flask(__name__)
app.secret_key = "secret_key_here"

def get_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="flask_auth",
        cursorclass=pymysql.cursors.DictCursor
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
        
        print(f"Received data - Username: {username}, Email: {email}, Password: {password}")

        try:
            conn = get_db()
            print("Database connection successful")
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                (username, email, password)
            )
            conn.commit()
            print("Data inserted successfully")
            conn.close()
            return redirect(url_for("login"))
        except Exception as e:
            print(f"Error: {e}")
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


if __name__ == "__main__":
    app.run(debug=True)