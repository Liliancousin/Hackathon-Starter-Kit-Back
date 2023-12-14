from sqlalchemy import Column, String, Integer

from shared import db


class CouleurModel(db.Model):

    __tablename__ = "couleur"
 
    id = Column(
	Integer, 
	primary_key=True, 
	unique=True, 
	nullable=False

    )

    nom_taille = Column(
	String(45), 
	nullable=False, 
	unique=True

    )
    message = Column(String(100))
