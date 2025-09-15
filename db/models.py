from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from db_session import Base

class Messages(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    id_user = Column(Integer)
    id_message = Column(Integer)
    text_message = Column(String)