# Project Night City - Personal Portfolio

A Django personal portfolio website with a public side (introduction, skills, projects, contact, testimonies) and an admin-only dashboard for managing projects and tech stacks.

---

## What You Need Before Starting

- Python 3.10 or newer installed
- Git installed
- A terminal (PowerShell on Windows, Terminal on Mac/Linux)

To check Python is installed, run:

    python --version

---

## How to Run the Project (Step by Step)

### Step 1 - Clone the repository

    git clone [github.com](https://github.com/Carlos-176/Project-Night-City.git)
    cd Project-Night-City/Coding/Portfolio

### Step 2 - Create a virtual environment

Windows (PowerShell):

    python -m venv venv
    .\venv\Scripts\Activate.ps1

Mac / Linux:

    python3 -m venv venv
    source venv/bin/activate

You will know it worked when you see (venv) at the start of your terminal line.

### Step 3 - Install the requirements

    python -m pip install -r requirements.txt

### Step 4 - Set up the environment file

Copy the example file to create your own .env:

Windows (PowerShell):

    Copy-Item .env.example .env

Mac / Linux:

    cp .env.example .env

Open the new .env file and make sure it looks like this:

    SECRET_KEY=django-insecure-local-dev-key
    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1,localhost

### Step 5 - Run the database migrations

    python manage.py migrate

Note: this is migrate, not makemigrations. The migration files are already in the repository, so you only need to apply them.

### Step 6 - Create an admin account

    python manage.py createsuperuser

Enter a username, email (can be skipped by pressing Enter), and password. Remember these details - you will need them to sign in.

### Step 7 - Start the server

    python manage.py runserver

Open your browser and go to:

    [127.0.0.1](http://127.0.0.1:8000/)

---

## How to Use the Site

### Public pages (anyone can view)

- / - Introduction / home page
- /skills/ - Skills page
- /projects/ - List of all projects
- /personal-info/ - Personal information
- /contact/ - Contact form
- /testimonies/ - Testimonies list and submission form

### Admin pages (superuser only)

- /login/ - Admin sign-in page. Only superuser accounts can log in here.
- /dashboard/ - Dashboard with the Projects table and Tech Stacks table
- /dashboard/projects/ - Full projects table
- /dashboard/tech-stacks/ - Full tech stacks table
- /dashboard/projects/create/ - Add a new project
- /dashboard/tech-stacks/create/ - Add a new tech stack

After signing in at /login/, you are redirected straight to /dashboard/.

Steps to add data:

1. Go to /login/ and sign in with your superuser account.
2. Click "+ ADD TECH STACK" and add a tech stack (for example, Python).
3. Click "+ ADD PROJECT", fill in the fields, and pick the tech stack using the radio button.
4. The new project will appear on the dashboard and on the public /projects/ page.

---

## Environment Variables

This project uses python-decouple to keep sensitive values out of the code.

- .env.example is committed to the repository and shows which variables are needed.
- .env holds your real values and is NOT committed (it is listed in .gitignore).

Variables used:

- SECRET_KEY - Django secret key
- DEBUG - True for development, False for production
- ALLOWED_HOSTS - comma-separated list of allowed hostnames

---

## Notes

- The database file db.sqlite3 is not included in the repository. It is created when you run python manage.py migrate.
- The virtual environment folder venv/ is not included either. You create your own.
- Only superuser accounts can access the dashboard. Regular user accounts are rejected at the login page.

---

## Author

Carlos Angelo M. Galang
