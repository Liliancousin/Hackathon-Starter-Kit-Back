""" Routes for the endpoint 'taille'"""

from flask import Blueprint, request
from marshmallow import ValidationError

from data.tailles.models import TailleModel
from data.tailles.schemas import TailleSchema
from shared import db

NAME = 'taille'

taille_blueprint = Blueprint(f"{NAME}_taille_blueprint", __name__)


@taille_blueprint.get(f"/taille/<int:id>")
def get_taille(id: str):
    """GET route code goes here"""
    entity: TailleModel = db.session.query(TailleModel).get(id)
    if entity is None:
        return "Goodby, World.", 404
    return entity.message, 200


@taille_blueprint.post(f"/taille/")
def post_taille():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: TailleModel = TailleSchema().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid TailleModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return TailleSchema().dump(entity), 200


@taille_blueprint.delete(f"/taille/<int:id>")
def delete_taille(id: str):
    """DELETE route code goes here"""
    return "Unimplemented", 501


@taille_blueprint.put(f"/taille/<int:id>")
def put_taille(id: str):
    """PUT route code goes here"""
    return "Unimplemented", 501


@taille_blueprint.patch(f"/taille/<int:id>")
def patch_taille(id: str):
    """PATCH route code goes here"""
    return "Unimplemented", 501
