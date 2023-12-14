"""Schema for serializing/deserializing a PanierModel"""

from data.paniers.models.panier_model import PanierModel
from shared.utils.schema.base_schema import BaseSchema


class PanierSchema(BaseSchema):
    class Meta:
        model = PanierModel
        load_instance = True
