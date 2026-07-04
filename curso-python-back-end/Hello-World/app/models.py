from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Message(Base):
    __tablename__ = "Message"
    id_message = Column("ID_MESSAGE", Integer, primary_key=True, autoincrement=True)
    content = Column("CONTENT", String(255), nullable=False)

