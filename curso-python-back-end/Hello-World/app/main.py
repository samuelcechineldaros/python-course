from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database

app = FastAPI(title="Hello World API")

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    yield from database.get_db()

@app.get("/")
async def read_root():
    return {"Mensagem": "Hello World"}

@app.get("/messages", response_model=list[schemas.MessageOut])
def read_messages(db: Session = Depends(get_db)):
    messages = db.query(models.Message).all()
    return [
        {
            "id_message": message.id_message,
            "content": message.content,
        }
        for message in messages
    ]

@app.get("/messages/{message_id}", response_model=schemas.MessageOut)
def read_message(message_id: int, db: Session = Depends(get_db)):
    message = db.query(models.Message).filter(models.Message.id_message == message_id).first()
    if message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return {
        "id_message": message.id_message,
        "content": message.content,
    }

@app.post("/messages", response_model=schemas.MessageOut)
def create_message(message: schemas.MessageCreate, db: Session = Depends(get_db)):
    db_message = models.Message(
        content=message.content
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return {
        "id_message": db_message.id_message,
        "content": db_message.content,
    }
