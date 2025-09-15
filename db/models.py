from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from db.db_session import Base
from sqlalchemy.orm import relationship, declarative_base

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    id_tg = Column(Integer)

    messages = relationship("Messages", back_populates="user")

class Messages(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey("users.id"))
    id_message = Column(Integer)
    text_message = Column(String)

    user = relationship("Users", back_populates="messages")