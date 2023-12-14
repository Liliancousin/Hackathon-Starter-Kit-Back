from sqlalchemy import Column, String, Integer, ForeignKey, relationship

from shared import db


class PanierModel(db.model):
    __tablename__ = "panier"
 
    id = Column(
	Integer, 
	primary_key=True,
    nullable=False,
	autoincrement=True
    )
    prix_panier = Column(
	Integer, 
	nullable=False
    )
    vetement_id = Column(
	Integer, ForeignKey('vetement.id'), 
	nullable=False
    )
    user_id = Column(
	Integer, 
	ForeignKey('user.id'), 
	nullable=False
    )
 
    VetementModel = relationship('VetementModel', back_populates='PanierModel')
    UserModel = relationship('UtilisateurModel', back_populates='PanierModel')

    message = Column(String(100))
