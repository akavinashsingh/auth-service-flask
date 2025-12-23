# Flask Authentication System (MySQL)

A simple **Flask-based authentication system** with **MySQL database integration**, providing user **signup, login, and home pages**.
This project is beginner-friendly and suitable for **college mini projects**, **learning backend integration**, and **Flask + MySQL practice**.

---

## 🚀 Features

* User Registration (Signup)
* User Login Authentication
* MySQL Database Integration
* Secure Password Handling
* Simple HTML Frontend
* Easy Project Setup & Deployment

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML
* **Database:** MySQL
* **Tools:** VS Code / PyCharm, MySQL Server

---

## 📂 Project Structure

```
project-root/
│
├── app.py              # Flask backend
├── schema.sql          # MySQL database schema
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

## 🧑‍💻 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/repo-name.git
cd repo-name
```

### 2️⃣ Install Required Packages

```bash
pip install flask mysql-connector-python
```

### 3️⃣ Setup MySQL Database

1. Open MySQL
2. Create a database:

```sql
CREATE DATABASE auth_db;
```

3. Import schema:

```bash
mysql -u root -p auth_db < schema.sql
```

---

### 4️⃣ Configure Database in `app.py`

Update your MySQL credentials:

```python
host="localhost"
user="root"
password="your_password"
database="auth_db"
```

---

### 5️⃣ Run the Application

```bash
python app.py
```

Visit:

```
http://127.0.0.1:5000
```

---

## 🔐 Authentication Flow

1. User signs up → data stored in MySQL
2. User logs in → credentials verified
3. On success → redirected to home page
4. On failure → error message shown

---

## 📌 Use Cases

* College Mini Project
* Flask Learning Project
* Backend Practice
* Authentication System Demo
* Resume / Portfolio Project

---

## 📈 Future Enhancements

* Password hashing using `bcrypt`
* Session management & logout
* Email verification
* Role-based access (Admin/User)
* Bootstrap or Tailwind UI
* JWT Authentication

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is open-source and free to use for educational purposes.

