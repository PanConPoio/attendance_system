# 📚 Attendance Management System

⚠️ Note: Only attendance_system.py is included in this repository. All required files such as users.json, config.json, attendance.json, and language files are automatically generated when the program is run for the first time.

This repository contains a desktop application built with Python to manage student attendance efficiently. It features a modern graphical interface, animations, user roles, and multilingual support.

## ✨ Key Features
🔐 Secure login system with SHA256 password hashing

👤 User roles: Admin, Teacher, and Student

👥 User management: create, delete, and authenticate users

📅 Daily attendance recording by student

✏️ Edit attendance by date and student

📊 Generate detailed attendance statistics

📁 Export attendance data to CSV

🧾 Submit absence justifications with attachments

🔍 Search and filter capabilities in user and attendance lists

🎨 Light and Dark theme support

🌐 Multilingual interface: English 🇺🇸 and Spanish 🇪🇸

🎞️ UI animations (fade, slide, shake, typewriter, etc.)

🗃️ Recent activity dashboard

📆 Date picker using tkcalendar

🧩 Modern GUI with ttkthemes

⚙️ Dynamic dashboard based on user roles

## 📁 File Structure
```
├── attendance_system.py         # Main system file

├── config.json                  # Stores theme/language/setup config

├── users.json                   # User data

├── attendance.json              # Attendance records

├── justifications.json          # Absence justifications

└── languages
    
    ├── es.json                  # Spanish translations
    
    └── en.json                  # English translations
```
## 🛠 Requirements
Python 3.8 or higher
```
pip install ttkthemes tkcalendar
```

## ▶️ How to Run
```
python attendance_system.py
```

## 🔐 Role-based Functionalities
### 👑 Admin
Manage all users

View and edit attendance records

Access dashboards and statistics

Export data and configure settings

### 👨‍🏫 Teacher
Record and review daily attendance

View and respond to student justifications

### 👨‍🎓 Student
View personal attendance history

Submit absence justifications with attachments

Access attendance analytics

## 🧪 Extra Functionalities
💾 Data persistence with JSON

🎨 Theme switching (light/dark) in real time

📈 Attendance analytics and reporting

🖨️ Print or export summaries

⚙️ Settings panel with live updates

✅ Form validation and user-friendly errors

---

📄 License
MIT License © 2025

Made with 💙 by Danlevy Hidalgo
