"""Core libs"""
from pydantic import (
    BaseModel,
    field_validator,
    ValidationError,
    model_validator,
    computed_field,
)


# custom validators
class User(BaseModel):
    """User class model"""

    username: str

    @field_validator("username")
    def username_length(self, val):
        """Function printing python version."""

        if len(val) < 4:
            raise ValidationError("Username must contains at least 4 character")
        return val


class SignUpData(BaseModel):
    """sign up data"""

    password: str
    confirm_password: str

    @model_validator(mode="after")
    def password_math(self, values):
        """Matches the password and confirm pass"""

        if values.password != values.confirm_password:
            raise ValidationError("Your confirm password does not match")
        return values


class Product(BaseModel):
    """Product info"""

    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        """Return total price"""

        return self.price * self.quantity
