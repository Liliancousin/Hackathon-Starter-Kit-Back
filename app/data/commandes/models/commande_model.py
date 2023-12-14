from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, relationship

from shared import db


class CommandeModel(db.Model):
    __tablename__ = "commande"
 
    id = Column(
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
    date_commande = Column(
	DateTime, 
	nullable=False
    )
    panier_id = Column(
	Integer, 
	ForeignKey('panier.id'), 
	nullable=False
    )
    PanierModel = relationship('PanierModel', back_populates='commande'),

message = Column(String(100))
