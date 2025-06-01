@echo off

REM Set the project directory
SET PROJECT_DIR=%~dp0

REM Navigate to the project directory
cd /d %PROJECT_DIR%

IF EXIST db.sqlite3 (
    REM Delete the db.sqlite3 file
    del db.sqlite3
)

IF EXIST django.log (
    REM Delete the django.log file
    del django.log
)

REM Check if virtual environment exists
IF NOT EXIST .venv (
    REM Create virtual environment
    python -m venv .venv
)

REM Activate the virtual environment
call .venv\Scripts\activate

REM Install dependencies from requirements.txt
IF EXIST requirements.txt (
    pip install -r requirements.txt
) ELSE (
    echo "requirements.txt not found!"
    exit /b 1
)

REM Apply makemigrations
python manage.py makemigrations

REM Apply migrations
python manage.py migrate

REM Run the development server
python manage.py runserver 8080

REM Deactivate the virtual environment after server stops
CALL .venv\Scripts\deactivate

PAUSE
