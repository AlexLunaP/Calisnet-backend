from typing import TypedDict


class UserDTO(TypedDict):
    userId: str
    username: str
    userEmail: str
    userPassword: str
