"""Schema for serializing/deserializing a VetementModel"""

from data.vetements.models.vetement_model import VetementModel
from shared.utils.schema.base_schema import BaseSchema


class VetementSchema(BaseSchema):
    class Meta:
        model = VetementModel
        load_instance = True
