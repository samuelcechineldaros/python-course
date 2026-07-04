# Python Back-end Project

This is a basic FastAPI back-end project.

## Setup

1. Install dependencies:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

2. Initialize the database (creates `Hello-World.db` from `Hello-World.db.sql`):

   ```bash
   python3 scripts/init_db.py
   ``` 

3. Run the application:

   ```bash
   uvicorn app.main:app --reload
   ```

4. Open your browser to `http://127.0.0.1:8000` to see the API documentation at `http://127.0.0.1:8000/docs`

## Endpoints

- `GET /`: Returns {"Hello": "World"}
- `GET /messages`: Returns list messages
- `GET /messages/{messages_id}`: Returns messages by id
- `POST /messages`: Creates a new message