"""Schema for serializing/deserializing a TailleModel"""

from data.tailles.models.taille_model import TailleModel
from shared.utils.schema.base_schema import BaseSchema


class TailleSchema(BaseSchema):
    class Meta:
        model = TailleModel
        load_instance = True
