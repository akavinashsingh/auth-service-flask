
# Flask Authentication System (MySQL + Railway)

A simple **Flask-based authentication system** with **MySQL database integration**, supporting **user signup, login, and session-based authentication**.
The project is beginner-friendly and suitable for **college mini projects**, **backend learning**, and **Flask + MySQL practice**.

This application supports **both local MySQL** and **Railway-hosted MySQL** for easy cloud deployment.

---

## 🚀 Features

* User Registration (Signup)
* User Login Authentication
* MySQL Database Integration
* Environment Variable–based DB Configuration
* Railway Cloud Database Support
* Simple HTML Frontend
* Easy Local & Cloud Deployment



## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML
* **Database:** MySQL (Local / Railway)
* **Deployment:** Railway / Render
* **Tools:** VS Code, Git, MySQL

---

## 📂 Project Structure

```
project-root/
│
├── app.py              # Flask backend
├── schema.sql          # MySQL database schema
├── requirements.txt    # Python dependencies
│
├── templates/
│   ├── index.html      # Landing page
│   ├── signup.html     # Signup page
│   ├── login.html      # Login page
│   └── home.html       # Home page
│
└── README.md
```

---

## 🧑‍💻 Local Setup (MySQL)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/repo-name.git
cd repo-name
```

---

### 2️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Setup MySQL Database

```sql
CREATE DATABASE auth_db;
```

Import schema:

```bash
mysql -u root -p auth_db < schema.sql
```

---

### 4️⃣ Run the Application

```bash
python app.py
```

Visit:

```
http://127.0.0.1:5000
```

---

## ☁️ Railway MySQL Setup (Recommended for Deployment)

### 1️⃣ Create MySQL Service on Railway

* Go to **[https://railway.app](https://railway.app)**
* Create a new project
* Add **MySQL** service
* Railway automatically creates a database

---

### 2️⃣ Connect MySQL to Flask App

In your **Flask App Service → Variables**, add:

| Variable       | Value                    |
| -------------- | ------------------------ |
| `DATABASE_URL` | `${{ MySQL.MYSQL_URL }}` |
| `SECRET_KEY`   | any-random-string        |

> This uses **Railway private networking** (no egress cost).

---

### 3️⃣ Deploy Flask App

* Push your code to GitHub
* Connect the repo to **Railway or Render**
* Set start command:

  ```bash
  gunicorn app:app
  ```
* Railway automatically installs dependencies and starts the app

---

## 🔐 Database Configuration (How it Works)

* Locally → connects to **localhost MySQL**
* On Railway → connects via `DATABASE_URL`
* No hardcoded credentials
* Safe for GitHub and production use

---

## 🔄 Authentication Flow

1. User signs up → data stored in MySQL
2. User logs in → credentials verified
3. Successful login → redirected to home page
4. Logout clears session

---

## 📌 Use Cases

* College Mini Project
* Flask Backend Learning
* MySQL Integration Practice
* Authentication System Demo
* Resume / Portfolio Project

---

## 📈 Future Enhancements

* Password hashing (bcrypt / werkzeug)
* Email verification
* Role-based access (Admin/User)
* Bootstrap / Tailwind UI
* JWT Authentication
* Forgot Password flow

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is open-source and free to use for **educational purposes**.

---

### ⭐ If this project helped you, consider starring the repo!

