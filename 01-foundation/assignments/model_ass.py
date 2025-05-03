# TODO: Create Booking model
# Fields:
# - user_id: int
# - room_id: int
# - nights: int (must be >=1)
# - rate_per_night: float
# Also, add computed field: total_amount = nights * rate_per_night


from pydantic import BaseModel, Field, computed_field


class Booking(BaseModel):
    """Handles booking validations"""

    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_pre_night: float

    @computed_field
    @property
    def total_amount(self) -> float:
        """computes total amount to be charged"""
        return self.rate_pre_night * self.nights

    # @field_validator("nights")
    # def validate_nights(self, val):
    #     """validate nights"""
    #     if val <= 0:
    #         raise ValidationError("Nights can't be negative")
    #     return val
