from typing import TypedDict


class UserDTO(TypedDict):
    userId: str
    username: str
    userEmail: str
    userPassword: str
    bio: str
    birthdate: str
    profilePicUrl: str
    socialLinks: dict
    competitionHistory: list
    achievements: list
