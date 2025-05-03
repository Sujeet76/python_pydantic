from datetime import datetime
from pydantic import BaseModel, ConfigDict


class Address(BaseModel):
    """Address validator"""

    street: str
    city: str
    zip_code: str


class User(BaseModel):
    """user validator"""

    id: int
    name: str
    is_active: bool
    created_at: datetime
    address: Address
    tag: list[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S")}
    )


user = User(
    id=1,
    name="sujeet",
    is_active=True,
    created_at=datetime(2025, 4, 15, 14, 30),
    address=Address(street="some street", city="Jaipur", zip_code="001144"),
    tag=["some", "some2"],
)

# Using model_dump() -> dict
python_dict = user.model_dump()

print(python_dict)


python_json = user.model_dump_json()
print(python_json)
