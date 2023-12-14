""" Routes for the endpoint 'news'"""

from flask import Blueprint, request
from marshmallow import ValidationError

from data.newss.models import NewsModel
from data.newss.schemas import NewsSchema
from shared import db

NAME = 'news'

news_blueprint = Blueprint(f"{NAME}_news_blueprint", __name__)


@news_blueprint.get(f"/news/<int:id>")
def get_news(id: str):
    """GET route code goes here"""
    entity: NewsModel = db.session.query(NewsModel).get(id)
    if entity is None:
        return "Goodby, World.", 404
    return entity.message, 200


@news_blueprint.post(f"/news/")
def post_news():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: NewsModel = NewsSchema().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid NewsModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return NewsSchema().dump(entity), 200


@news_blueprint.delete(f"/news/<int:id>")
def delete_news(id: str):
    """DELETE route code goes here"""
    return "Unimplemented", 501


@news_blueprint.put(f"/news/<int:id>")
def put_news(id: str):
    """PUT route code goes here"""
    return "Unimplemented", 501


@news_blueprint.patch(f"/news/<int:id>")
def patch_news(id: str):
    """PATCH route code goes here"""
    return "Unimplemented", 501
