from sqlalchemy import Column, String, Integer, DateTime

from shared import db


class UserModel(db.Model):
    __tablename__ = "user"
    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        nullable=False,

    )
    nom_utilisateur = Column(
        String(45),
        nullable=False,
    )
    email_utilisateur = Column(
        String(45),
        nullable=False,
        unique=True,
    )
    date_de_naissance = Column(
        DateTime,
        nullable=False,
    )
    mot_de_passe = Column(
        String(45),
        nullable=False
    )
    event_id = Column(
	    Integer, 
	    ForeignKey('event.id'), 
	    nullable=False
    )
 
    EventModel = relationship('EventModel', back_populates='UserModel')
    

    message = Column(String(100))
