# Health Management System (Flask + MySQL/SQLite + Bootstrap 5)

A modern, full-stack **Health Management System (HMS)** built with Flask, Bootstrap 5, Chart.js, DataTables, SweetAlert2, and SQLAlchemy.

---

## 🌟 Key Features

### 1. **Authentication & Role Control**
- Role-based Dashboard & System Access (**User/Patient** vs **Admin**).
- Password hashing with **Flask-Bcrypt**.
- Form validation via **Flask-WTF** with CSRF Protection.
- Unique email and phone number enforcement.

### 2. **User (Patient) Features**
- **Dashboard**: High-level statistics (Reports, Bills, Family Members, Last Upload), Chart.js yearly upload analytics, recent vitals widget.
- **Profile Management**: Update personal info, blood group, emergency contact, residential address, and profile photo upload.
- **Family Members Module**: Full CRUD operations to manage health profiles of relatives.
- **Medical Reports Module**: Upload PDF/PNG/JPG reports (≤10MB) with hospital, doctor, and report type metadata. In-browser document preview, file download, and delete.
- **Medical Bills Module**: Record hospital bills, pharmacy receipts, and track payment status (Paid, Pending, Overdue).
- **Health Vitals & BMI Tracker**: Log height/weight with automated BMI calculation, systolic/diastolic blood pressure, and fasting blood sugar level tracking.

### 3. **Admin Features**
- **Admin Dashboard**: System-wide statistics, user registration metrics chart, report upload analytics, and recent activity logs.
- **User Management**: Searchable/sortable DataTables list of patients. Activate/deactivate user accounts, reset user passwords, and delete accounts.
- **System-wide Reports & Bills**: Comprehensive oversight of all patient uploads across the application with multi-filtering.

### 4. **Modern Design System**
- Responsive layout with glassmorphism card components, custom vibrant gradients, and Google Fonts (Inter).
- Dynamic **Dark/Light Mode Theme Toggle** (persisted across sessions).
- Interactive SweetAlert2 deletion confirmation modals and Toast notifications.

---

## 🚀 Quick Start Guide

### 1. Prerequisites
- Python 3.9+
- pip package manager

### 2. Installation
Navigate to the project root directory and install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Database Setup

By default, the application runs on **SQLite** (`app.db`) for instant zero-config setup.

To switch to **MySQL**:
1. Create a MySQL database (e.g. `CREATE DATABASE hms_db;`).
2. Update `config.py` or set the environment variable:
   ```python
   SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/hms_db'
   ```

### 4. Seed Initial Data & Run App

Run `run.py` to create database tables, seed demo data, and launch the dev server:

```bash
python run.py
```

Open your browser at: **`http://127.0.0.1:5000`**

---

## 🔑 Default Logins

| Role | Email | Password |
| :--- | :--- | :--- |
| **Admin** | `admin@hms.com` | `Admin@123` |
| **Patient (User)** | `patient@hms.com` | `Patient@123` |

---

## 📁 Directory Structure

```text
HMS2/
├── app/
│   ├── auth/            # Authentication blueprint (Login/Signup/Logout)
│   ├── admin/           # Admin blueprint (User management, system reports & bills)
│   ├── user/            # User blueprint (Dashboard, profile, family, reports, bills, vitals)
│   ├── templates/       # HTML5 Jinja templates
│   ├── static/          # CSS, JS, Images
│   ├── models.py        # SQLAlchemy database schemas
│   ├── utils.py         # Admin decorator, file upload handlers
│   └── __init__.py      # App factory & extension initialization
├── uploads/             # Secure storage for reports, bills, profile photos
├── config.py            # App settings & limits
├── run.py               # Application entrypoint & seeder
└── requirements.txt     # Python dependencies
```
