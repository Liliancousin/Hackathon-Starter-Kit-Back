from sqlalchemy import Column, String, Integer, ForeignKey, relationship

from shared import db


class VetementModel(db.model):
    __tablename__ = "vetement"
 
    id_vetement = Column(
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
    id_couleur = Column(
	Integer, 
	ForeignKey('idCouleur'), 
	nullable=False
    )
    id_taille = Column(
	Integer, 
	ForeignKey('idTaille'), 
	nullable=False
    )
 
    taille = relationship('Taille', back_populates='vetements')
    couleur = relationship('Couleur', back_populates='vetements')
    message = Column(String(100))
