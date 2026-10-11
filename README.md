# Django Hotel Request Tracker

This is a small Django application created for my Capstone Research Milestone.

Users can submit a hotel service request with a room number, request type, and details. Requests are saved in Django's SQLite database and displayed on a request queue page. The Django admin page can be used to update request statuses.

## Run the project

1. Activate the virtual environment:
   `.venv\Scripts\activate`

2. Install dependencies:
   `py -m pip install -r requirements.txt`

3. Run migrations:
   `py manage.py migrate`

4. Start the server:
   `py manage.py runserver`