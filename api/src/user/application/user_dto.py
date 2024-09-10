from typing import TypedDict


class UserDTO(TypedDict):
    user_id: str
    user_email: str
    user_password: str
    username: str
    full_name: str
    bio: str
    profile_pic_url: str
    social_links: dict
