# 🌐 MyBlog — A Modern Django Blogging Platform

> **MyBlog** is a full-featured blogging web application built with Django that allows users to create accounts, publish posts, manage profiles, and securely reset passwords via email. It’s designed with clean UI, secure authentication, and production-ready practices.

---

## ✨ Features

### 🔐 Authentication System

* User registration and login
* Secure logout functionality
* Password reset via email verification
* Encrypted password storage using Django auth system

### 📝 Blog Functionality

* Create new blog posts
* Edit and update your posts
* Delete your posts
* View all posts from all users
* View posts by specific authors

### 👤 User Profile

* Dedicated profile page
* Update user information
* Profile management support

### 📧 Email Integration

* Password reset via Gmail SMTP
* Secure token-based password reset links
* Environment variable protection using `.env`

### 🎨 User Interface

* Clean and modern Bootstrap design
* Responsive layout for all devices
* Easy and intuitive navigation

---

## 🛠️ Tech Stack

**Backend**

* Django
* Python

**Frontend**

* HTML
* CSS
* Bootstrap

**Database**

* SQLite (default)
* PostgreSQL (production ready)

**Other Tools**

* Django Crispy Forms
* Python Dotenv
* Gunicorn (deployment ready)

---

## ⚙️ Installation Guide

### 1. Clone the repository

```
git clone https://github.com/yourusername/MyBlog.git
cd MyBlog
```

---

### 2. Create virtual environment

```
python -m venv venv
```

Activate environment:

**Windows**

```
venv\Scripts\activate
```

**Linux / Mac**

```
source venv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Create environment variables file

Create a `.env` file and add:

```
SECRET_KEY=your_secret_key
DEBUG=True

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

---

### 5. Apply migrations

```
python manage.py migrate
```

---

### 6. Run the development server

```
python manage.py runserver
```

Open your browser and go to:

```
http://127.0.0.1:8000/
```

---

## 🔑 Password Reset System

MyBlog includes a secure password reset system:

* User requests password reset
* Email sent with secure reset link
* User creates new password
* Account updated safely

---

## 🚀 Deployment Ready

This project can be deployed on:

* Render
* Railway
* PythonAnywhere
* Fly.io

---

## 🔒 Security Features

* CSRF protection
* Secure password hashing
* Token-based password reset
* Environment variable protection
* Django built-in security protections

---

## 🎯 Learning Objectives

This project demonstrates:

* Real-world Django development
* Authentication and authorization
* Email integration
* Secure web development practices
* Production-ready Django setup

---

## 👨‍💻 Author

**Nayan**

GitHub: https://github.com/nayan1205
Email: [nyngtm@gmail.com](mailto:nyngtm@gmail.com)

---

## ⭐ Support

If you found this project useful, please consider giving it a star ⭐ on GitHub.

---

## 📜 License

This project is open source and available for learning and educational purposes.

---

**MyBlog — Share your thoughts with the world.**
