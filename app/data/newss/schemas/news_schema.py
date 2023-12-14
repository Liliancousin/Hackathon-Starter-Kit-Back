"""Schema for serializing/deserializing a NewsModel"""

from data.newss.models.news_model import NewsModel
from shared.utils.schema.base_schema import BaseSchema


class NewsSchema(BaseSchema):
    class Meta:
        model = NewsModel
        load_instance = True
