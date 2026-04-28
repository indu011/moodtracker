# 😊 Mood Tracker Web Application

A simple and interactive Mood Tracker web application built using **Python Flask**, **HTML**, **CSS**, and **SQLite**.  
This application allows users to record their daily mood with emojis and notes, and view previous mood entries in a clean and modern UI.

---

## 🚀 Features

- 😊 Select mood using emoji buttons
- 📝 Add personal notes about the day
- 💾 Store mood entries in SQLite database
- 📜 View previous mood history
- 🎨 Modern glassmorphism UI design
- ⚡ Lightweight and beginner-friendly Flask project

---

## 🛠️ Technologies Used

- **Frontend**
  - HTML5
  - CSS3
  - JavaScript

- **Backend**
  - Python
  - Flask

- **Database**
  - SQLite3

---

## 📂 Project Structure

```bash
Mood-Tracker/
│
├── app.py
├── mood_tracker.db
├── moods.db
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/mood-tracker.git
cd mood-tracker
```

### 2️⃣ Install Flask

```bash
pip install flask
```

### 3️⃣ Run the Application

```bash
python app.py
```

### 4️⃣ Open in Browser

```bash
http://127.0.0.1:5000
```

---

## 📸 Application Workflow

1. User selects a mood emoji
2. User writes a short note
3. Mood entry gets saved into SQLite database
4. Previous entries are displayed on the homepage

---

## 🧠 Database Schema

| Column Name | Type |
|-------------|------|
| id | INTEGER |
| mood | TEXT |
| note | TEXT |
| emoji | TEXT |
| timestamp | DATETIME |

---

## 🎯 Future Enhancements

- 📊 Mood analytics dashboard
- 🔐 User authentication
- 🌙 Dark mode support
- 📅 Calendar-based mood history
- ☁️ Cloud database integration

---

## 👨‍💻 Author

Developed by **[Your Name]**

---

## 📄 License

This project is open-source and available under the MIT License.
