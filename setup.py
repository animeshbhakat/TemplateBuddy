# Import required libraries
import sqlite3
import os

def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)

if os.path.exists("local.db"):
    os.remove("local.db")

mkdir("static/rendered")
mkdir("static/rendered/resumes")
mkdir("static/images/profile_pictures")

# Setup connection to db
conn = sqlite3.connect("local.db")

# Create table - users
conn.execute(
    """CREATE TABLE users(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL
    )"""
)

# Create table - resume_details
conn.execute(
    """CREATE TABLE resume_details(
        id INTEGER PRIMARY KEY,
        uid INTEGER NOT NULL,

        firstname TEXT,
        middlename TEXT,
        lastname TEXT,
        email TEXT,
        mobile TEXT,
        address_1 TEXT,
        address_2 TEXT,
        city TEXT,
        state TEXT,
        zip TEXT,
        profile_picture TEXT,
        headline TEXT,
        github TEXT,
        linkedin TEXT,
        twitter TEXT,
        website TEXT,
        behance TEXT,
        dribble TEXT,
        summary TEXT,

        institute_names TEXT,
        cities TEXT,
        countries TEXT,
        degrees TEXT,
        fields_of_study TEXT,
        start_dates DATE,
        end_dates DATE,
        grade_types TEXT,
        grades TEXT,

        job_titles TEXT,
        companies TEXT,
        cities_exp TEXT,
        countries_exp TEXT,
        start_dates_exp TEXT,
        end_dates_exp TEXT,
        description TEXT,

        skill_names TEXT,

        project_title TEXT,
        description_proj TEXT,
        start_dates_proj TEXT,
        end_dates_proj TEXT,

        course_names TEXT,
        issuers TEXT,
        issues_on_dates TEXT,

        paper_titles TEXT,
        publications TEXT,
        published_on_dates TEXT,

        honor_titles TEXT,
        honor_issuers TEXT,
        honor_issued_dates TEXT,

        hobbies TEXT
    )"""
)

# Close the connection
conn.close()
