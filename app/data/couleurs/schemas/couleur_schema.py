"""Schema for serializing/deserializing a CouleurModel"""

from data.couleurs.models.couleur_model import CouleurModel
from shared.utils.schema.base_schema import BaseSchema


class CouleurSchema(BaseSchema):
    class Meta:
        model = CouleurModel
        load_instance = True
