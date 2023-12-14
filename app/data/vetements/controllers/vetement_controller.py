""" Routes for the endpoint 'vetement'"""

from flask import Blueprint, request
from marshmallow import ValidationError

from data.vetements.models import VetementModel
from data.vetements.schemas import VetementSchema
from shared import db

NAME = 'vetement'

vetement_blueprint = Blueprint(f"{NAME}_vetement_blueprint", __name__)


@vetement_blueprint.get(f"/vetement/<int:id>")
def get_vetement(id: str):
    """GET route code goes here"""
    entity: VetementModel = db.session.query(VetementModel).get(id)
    if entity is None:
        return "Goodby, World.", 404
    return entity.message, 200


@vetement_blueprint.post(f"/vetement/")
def post_vetement():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: VetementModel = VetementSchema().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid VetementModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return VetementSchema().dump(entity), 200


@vetement_blueprint.delete(f"/vetement/<int:id>")
def delete_vetement(id: str):
    """DELETE route code goes here"""
    return "Unimplemented", 501


@vetement_blueprint.put(f"/vetement/<int:id>")
def put_vetement(id: str):
    """PUT route code goes here"""
    return "Unimplemented", 501


@vetement_blueprint.patch(f"/vetement/<int:id>")
def patch_vetement(id: str):
    """PATCH route code goes here"""
    return "Unimplemented", 501
