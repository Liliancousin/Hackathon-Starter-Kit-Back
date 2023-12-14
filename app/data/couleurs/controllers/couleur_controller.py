""" Routes for the endpoint 'couleur'"""

from flask import Blueprint, request
from marshmallow import ValidationError

from data.couleurs.models import CouleurModel
from data.couleurs.schemas import CouleurSchema
from shared import db

NAME = 'couleur'

couleur_blueprint = Blueprint(f"{NAME}_couleur_blueprint", __name__)


@couleur_blueprint.get(f"/couleur/<int:id>")
def get_couleur(id: str):
    """GET route code goes here"""
    entity: CouleurModel = db.session.query(CouleurModel).get(id)
    if entity is None:
        return "Goodby, World.", 404
    return entity.message, 200


@couleur_blueprint.post(f"/couleur/")
def post_couleur():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: CouleurModel = CouleurSchema().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid CouleurModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return CouleurSchema().dump(entity), 200


@couleur_blueprint.delete(f"/couleur/<int:id>")
def delete_couleur(id: str):
    """DELETE route code goes here"""
    return "Unimplemented", 501


@couleur_blueprint.put(f"/couleur/<int:id>")
def put_couleur(id: str):
    """PUT route code goes here"""
    return "Unimplemented", 501


@couleur_blueprint.patch(f"/couleur/<int:id>")
def patch_couleur(id: str):
    """PATCH route code goes here"""
    return "Unimplemented", 501
