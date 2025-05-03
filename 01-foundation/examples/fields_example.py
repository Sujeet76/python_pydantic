from pydantic import BaseModel, Field


class Cart(BaseModel):
    """Class def"""

    user_id: int
    items: list[str]
    quantities: dict[str, int]


class Employee(BaseModel):
    """class def"""

    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee name is required",
        examples="Sujeet Kumar",
    )
    department: str = "General"
    salary: float = Field(..., ge=10)
