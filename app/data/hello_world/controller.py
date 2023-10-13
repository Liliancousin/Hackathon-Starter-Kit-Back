from flask import Blueprint, Response, request

from data.hello_world.model import HelloWorldModel
from data.hello_world.schema import HelloWorldSchema
from data.common import BaseCRUDHelper
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from shared import generate_token

NAME = 'helloworld'
blueprint = Blueprint(NAME + "_blueprint", __name__)

crud = BaseCRUDHelper(HelloWorldModel, HelloWorldSchema())

@blueprint.get('/login')
def settoken():
    return generate_token('Gwilhoa', "ca marche", 2)
@blueprint.get('/' + NAME + "/<uuid:id>")
def get_hello_world(id):
    return crud.handle_get(id)


@blueprint.post('/' + NAME)
def post_hello_world():
    data = request.get_json()
    return crud.handle_post(data)


@blueprint.delete('/' + NAME + "/<uuid:id>")
def delete_hello_world(id):
    return crud.handle_delete(id)


@blueprint.put('/' + NAME + "/<uuid:id>")
@jwt_required()
def update_hello_world(id):
    current_user = get_jwt_identity()
    print(current_user + " - " + get_jwt()["custom_data"], flush=True)
    data = request.get_json()
    return crud.handle_put(id, data)
