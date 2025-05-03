# TODO: Create Course model
# Each Course has modules
# Each Module has lessons

from pydantic import BaseModel


class Module(BaseModel):
    """Course module"""

    no_of_videos: int
    description: str
    name: str

class Course(BaseModel):
    """Course"""

    name: str
    desc: str
    modules: list[Module]

