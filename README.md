# Expense Tracker Web App

A full-stack expense tracking web application built using **Django** with integrated **Flask-based analytics**.

## Features

- User authentication (Register, Login, Logout)
- Add, view, and delete expenses
- Monthly expense summary
- Category-wise analytics with charts
- Flask-powered analytics page
- Export expenses as CSV
- Account settings (password change, delete account)

## Tech Stack

- **Backend:** Django, Flask
- **Frontend:** HTML, CSS, JavaScript, Chart.js
- **Database:** SQLite
- **Authentication:** Django Auth
- **Analytics:** Flask microservice

## Project Structure

## Running the Project (IMPORTANT)

This project uses TWO servers:

1. Django → Main application
2. Flask → Analytics microservice

### Steps

1. Clone repository
2. Create & activate virtual environment
3. Install dependencies
4. Run Django server
5. Run Flask analytics server (separately)

### Django
```bash
python manage.py migrate
python manage.py runserver

### Flask
cd flask_app
python app.py
