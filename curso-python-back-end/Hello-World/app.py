from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Mensagem": "Hello World"}

@app.get("/users/{user_id}")
async def read_user(user_id: int, q: str = None):
    return {"user_id": user_id, "user_name": q}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "item_name": q}