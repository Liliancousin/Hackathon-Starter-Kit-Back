from sqlalchemy import Column, String, Integer, DateTime

from shared import db


class NewsModel(db.Model):
    __tablename__ = "news"
    id = Column(
	Integer, 
	primary_key=True, 
	autoincrement=True
    )
    date_news = Column(
	DateTime, 
	nullable=False
    )
    nom_news = Column(
	String(45), 
	nullable=False
    )
    description_news = Column(
	String(45), 
	nullable=False
    )
    photo_news = Column(
	String(45), 
	nullable=False
	)
    lieu_news = Column(
	String(45), 
	nullable=False
   )
    message = Column(String(100))
