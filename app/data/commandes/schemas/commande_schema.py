"""Schema for serializing/deserializing a HelloWorldModel"""

from data.commandes.models.commande_model import CommandeModel
from shared.utils.schema.base_schema import BaseSchema


class CommandeSchema(BaseSchema):
    class Meta:
        model = CommandeModel
        load_instance = True
