# 🏥 Hospital Patient Record System

A web-based application built using **Flask (Python)** and **MySQL** to manage hospital records including **patients**, **doctors**, **appointments**, and **prescriptions**.

---

## 📌 Features

- 🧑‍⚕️ Add/View Patients
- 👨‍⚕️ Add/View Doctors
- 📅 Schedule Appointments
- 💊 Track Prescriptions & Visit History
- 📚 Relational DB Design with Foreign Keys & Joins

---

## 🛠️ Tech Stack

| Component     | Technology         |
|---------------|--------------------|
| Frontend      | HTML5              |
| Backend       | Flask (Python)     |
| Database      | MySQL              |
| Styling       | Basic HTML/CSS     |

---

## 📁 Project Structure


hospital_record_system/
│
├── app.py # Flask main app
├── requirements.txt # Python dependencies
├── hospital_db.sql # MySQL database schema
├── templates/ # HTML templates
│ ├── index.html
│ ├── patients.html
│ ├── doctors.html
│ ├── appointments.html
│ └── prescriptions.html
└── static/
└── style.css (optional)


---

## ✅ Steps to Run the Project

### 📦 Prerequisites

- Python 3.7 or higher
- MySQL Server
- Git (optional but recommended)

---

### 🔧 Step-by-Step Setup

### 1. 📥 Clone the Project

```bash
git clone https://github.com/your-username/hospital-record-system.git
cd hospital-record-system

2. 🐍 Create and Activate Virtual Environment (optional but recommended)

# For Linux/macOS
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate

3. 📦 Install Dependencies

pip install -r requirements.txt


4. 🗃️ Setup MySQL Database
Option A: Import SQL File
Open MySQL CLI or any GUI tool like phpMyAdmin / MySQL Workbench

Run the SQL commands in hospital_db.sql

SOURCE hospital_db.sql;

5. 🔐 Configure Database in app.py
Edit the MySQL credentials section:

db = mysql.connector.connect(
    host="localhost",
    user="your_mysql_username",
    password="your_mysql_password",
    database="hospital"
)

6. 🚀 Run the Flask App

python app.py

App will start on:

http://127.0.0.1:5000/

