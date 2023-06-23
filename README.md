
## Windows deployment

1. Download and install [Python3.10](https://www.python.org/downloads/)
2. Setup project
   1. Clone project folder
   2. Modify `.env` file and set config vairables
3. Open cmd and install poetry `pip install poetry`
4. Run `poetry config virtualenvs.in-project true`
5. Navigate to ***project root*** and run `poetry install`
6. Activate the environment `poetry shell`
7. Migrate database `python manage.py migrate`
8. Run python fastapi `uvicorn app.asgi:app --reload`