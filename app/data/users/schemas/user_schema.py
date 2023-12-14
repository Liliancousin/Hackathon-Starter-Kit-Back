"""Schema for serializing/deserializing a UserModel"""

from data.users.models.user_model import UserModel
from shared.utils.schema.base_schema import BaseSchema


class UserSchema(BaseSchema):
    class Meta:
        model = UserModel
        load_instance = True
