from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Message(Base):
    __tablename__ = "Message"
    id_message = Column("ID_MESSAGE", Integer, primary_key=True, autoincrement=True)
    content = Column("CONTENT", String(255), nullable=False)

