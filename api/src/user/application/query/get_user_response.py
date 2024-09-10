from typing import Optional


class GetUserResponse:
    def __init__(
        self,
        user_id: str,
        username: str,
        user_email: str,
        user_password: str,
        full_name: Optional[str] = None,
        bio: Optional[str] = None,
        profile_image_url: Optional[str] = None,
        social_links: Optional[dict] = None,
    ):
        self.__user_id: str = user_id
        self.__username: str = username
        self.__user_email: str = user_email
        self.__user_password: str = user_password
        self.__full_name: Optional[str] = full_name
        self.__bio: Optional[str] = bio if bio is not None else ""
        self.__social_links: Optional[dict] = (
            social_links if social_links is not None else {}
        )
        self.__profile_image_url: Optional[str] = profile_image_url

    @property
    def user_id(self):
        return self.__user_id

    @property
    def username(self):
        return self.__username

    @property
    def user_email(self):
        return self.__user_email

    @property
    def user_password(self):
        return self.__user_password

    @property
    def full_name(self):
        return self.__full_name

    @property
    def bio(self):
        return self.__bio

    @property
    def social_links(self):
        return self.__social_links

    @property
    def profile_image_url(self):
        return self.__profile_image_url

    @property
    def user_dto(self):
        return {
            "user_id": self.__user_id,
            "username": self.__username,
            "user_email": self.__user_email,
            "user_password": self.__user_password,
            "full_name": self.__full_name,
            "bio": self.__bio,
            "social_links": self.__social_links,
            "profile_image_url": self.__profile_image_url,
        }
