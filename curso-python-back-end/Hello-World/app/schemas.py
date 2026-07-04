from pydantic import BaseModel, Field, condecimal
from typing import Optional, List
from datetime import date

class MessageCreate(BaseModel):
    content: str

class MessageOut(MessageCreate):
    id_message: int