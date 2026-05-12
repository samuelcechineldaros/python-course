# Python Back-end Project

This is a basic FastAPI back-end project.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   uvicorn app:app --reload
   ```

3. Open your browser to `http://127.0.0.1:8000` to see the API documentation at `http://127.0.0.1:8000/docs`

## Endpoints

- `GET /`: Returns {"Hello": "World"}
- `GET /items/{item_id}`: Returns item details