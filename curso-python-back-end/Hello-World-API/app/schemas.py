from pydantic import BaseModel

class MessageCreate(BaseModel):
    content: str

class MessageOut(MessageCreate):
    id_message: int

class MessageUpdate(BaseModel):
    id_message: int
    content: str

class MessageDelete(BaseModel):
    id_message: int