""" Routes for the endpoint 'commande'"""

from flask import Blueprint, request
from marshmallow import ValidationError

from data.commandes.models import CommandeModel
from data.commandes.schemas import CommandeSchema
from shared import db

NAME = 'commande'

commande_blueprint = Blueprint(f"{NAME}_commande_blueprint", __name__)


@commande_blueprint.get(f"/commande/<int:id>")
def get_commande(id: str):
    """GET route code goes here"""
    entity: CommandeModel = db.session.query(CommandeModel).get(id)
    if entity is None:
        return "Goodby, World.", 404
    return entity.message, 200


@commande_blueprint.post(f"/commande/")
def post_commande():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: CommandeModel = CommandeSchema().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid CommandeModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return CommandeSchema().dump(entity), 200


@commande_blueprint.delete(f"/commande/<int:id>")
def delete_commande(id: str):
    """DELETE route code goes here"""
    return "Unimplemented", 501


@commande_blueprint.put(f"/commande/<int:id>")
def put_commande(id: str):
    """PUT route code goes here"""
    return "Unimplemented", 501


@commande_blueprint.patch(f"/commande/<int:id>")
def patch_commande(id: str):
    """PATCH route code goes here"""
    return "Unimplemented", 501
