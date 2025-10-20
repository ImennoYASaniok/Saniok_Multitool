from sqlalchemy import Column, Integer, String, ForeignKey
from db.db_session import Base
from sqlalchemy.orm import relationship
from decouple import config

class Users(Base):
    __tablename__ = 'users'
    __table_args__ = {"schema": config("POSTGRES_SCHEMA")}

    id = Column(Integer, primary_key=True)
    id_tg = Column(String, unique=True, index=True)

    messages = relationship("Messages", back_populates="user")

class Messages(Base):
    __tablename__ = 'messages'
    __table_args__ = {"schema": config("POSTGRES_SCHEMA")}

    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey(f"{config("POSTGRES_SCHEMA")}.users.id"))
    id_tg_message = Column(Integer, unique=True)
    text_message = Column(String)

    user = relationship("Users", back_populates="messages")