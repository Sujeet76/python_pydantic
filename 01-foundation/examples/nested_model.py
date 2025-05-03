from typing import Optional
from pydantic import BaseModel


class Address(BaseModel):
    """address"""

    street: str
    city: str
    postal_code: str

class User(BaseModel):
    """user"""

    id: int
    name: str
    address: Address

class Comment(BaseModel):
    """comment"""

    id: int
    content: str
    replies: Optional[list["Comment"]] = None

Comment.model_rebuild()

address = Address(
    street="123 something",
    city="Jaipur",
    postal_code="10001",
)

user = User(
    id=1,
    name="Sujeet",
    address=address,
)

comment = Comment(
    id=1,
    content="First Comment",
    replies=[Comment(id=2, content="reply1"), Comment(id=3, content="reply2")],
)

print("Address : ", address, "\n User : ", user, "\n Comment : ", comment)
