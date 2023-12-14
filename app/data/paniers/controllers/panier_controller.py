""" Routes for the endpoint 'panier'"""

from flask import Blueprint, request
from marshmallow import ValidationError

from data.paniers.models import PanierModel
from data.paniers.schemas import PanierSchema
from shared import db

NAME = 'panier'

panier_blueprint = Blueprint(f"{NAME}_panier_blueprint", __name__)


@panier_blueprint.get(f"/panier/<int:id>")
def get_panier(id: str):
    """GET route code goes here"""
    entity: PanierModel = db.session.query(PanierModel).get(id)
    if entity is None:
        return "Goodby, World.", 404
    return entity.message, 200


@panier_blueprint.post(f"/panier/")
def post_panier():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: PanierModel = PanierSchema().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid PanierModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return PanierSchema().dump(entity), 200


@panier_blueprint.delete(f"/panier/<int:id>")
def delete_panier(id: str):
    """DELETE route code goes here"""
    return "Unimplemented", 501


@panier_blueprint.put(f"/panier/<int:id>")
def put_panier(id: str):
    """PUT route code goes here"""
    return "Unimplemented", 501


@panier_blueprint.patch(f"/panier/<int:id>")
def patch_panier(id: str):
    """PATCH route code goes here"""
    return "Unimplemented", 501
