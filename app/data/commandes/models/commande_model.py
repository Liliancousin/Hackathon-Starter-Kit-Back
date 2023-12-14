from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, relationship

from shared import db


class CommandeModel(db.Model):
    __tablename__ = "commande"
 
    id_commmande = Column(
	Integer, 
	primary_key=True, 
	nullable=False
    )
    adresse_commande = Column(
	String(45), 
	nullable=False
    )
    numero_commande = Column(
	Integer, 
	autoincrement=True, 
	nullable=False
    )
    prix_total = Column(
	Integer, 
	nullable=False
    )
dateCommande = Column(
	DateTime, 
	nullable=False
    )
idPanier = Column(
	Integer, 
    ForeignKey('id_panier'), 
	nullable=False
    )
panier = relationship('panier', back_populates='commande'),

message = Column(String(100))
