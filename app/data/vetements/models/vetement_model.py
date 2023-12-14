from sqlalchemy import Column, String, Integer, ForeignKey, relationship

from shared import db


class VetementModel(db.model):
    __tablename__ = "vetement"
 
    id = Column(
	Integer, 
	primary_key=True, 
    	nullable=False,
	autoincrement=True
    )
    prix_vetement = Column(
	Integer, 
	nullable=False
    )
    description_vetement = Column(
	String(45), 
	nullable=False
    )
    couleur_id = Column(
	Integer, 
	ForeignKey('couleur.id'), 
	nullable=False
    )
    taille_id = Column(
	Integer, 
	ForeignKey('taille.id'), 
	nullable=False
    )
 
    TailleModel = relationship('TailleModel', back_populates='VetementModel')
    Couleur = relationship('CouleurModel', back_populates='VetementModel')
    message = Column(String(100))
