from sqlalchemy import Column, String, Integer, DateTime, relationship
from shared import db


class EventModel(db.Model):
    __tablename__ = "event"
 
    id = Column(
	Integer, 
	primary_key=True,
    unique=True,
    nullable=False, 
    )
    date_event = Column(
	DateTime, 
	nullable=False
    )
    nom_event = Column(
	String(45), 
	nullable=False
    )
    lieu_event = Column(
	String(45), 
	nullable=False
    )
    description_event = Column(
	String(45), 
	nullable=False
    )
    photo_event = Column(
	String(45), 
	nullable=False
    )
 
    UserModel = relationship('UserModel', back_populates='event')
    
    message = Column(String(100))
