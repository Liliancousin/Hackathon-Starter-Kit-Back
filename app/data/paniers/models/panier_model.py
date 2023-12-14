from sqlalchemy import Column, String, Integer, ForeignKey, relationship

from shared import db


class PanierModel(db.model):
    __tablename__ = "panier"
 
    id_panier = Column(
	Integer, 
	primary_key=True,
    nullable=False,
	autoincrement=True
    )
    prix_panier = Column(
	Integer, 
	nullable=False
    )
    id_vetement = Column(
	Integer, ForeignKey('idVetement'), 
	nullable=False
    )
    id_utilisateur = Column(
	Integer, 
	ForeignKey('utilisateur.idUtilisateur'), 
	nullable=False
    )
 
    vetement = relationship('Vetement', back_populates='paniers')
    utilisateur = relationship('Utilisateur', back_populates='paniers')

    message = Column(String(100))
