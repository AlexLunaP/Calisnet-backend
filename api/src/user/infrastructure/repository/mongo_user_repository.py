import os
from typing import Optional

import pymongo

from ....shared.domain.user_id import UserId
from ...domain.model.full_name import FullName
from ...domain.model.profile_image_url import ProfileImageUrl
from ...domain.model.social_links import SocialLinks
from ...domain.model.user import User
from ...domain.model.user_bio import UserBio
from ...domain.model.user_email import UserEmail
from ...domain.model.user_password import UserPassword
from ...domain.model.username import Username
from ...domain.repository.users import Users


class MongoUserRepository(Users):

    def __init__(self):
        self.__db = pymongo.MongoClient(os.environ["MONGODB_URL"])[
            os.environ["MONGODB_DBNAME"]
        ]
        self.__users = self.__db["users"]

    def save(self, user: User) -> None:
        self.__users.insert_one(
            {
                "user_id": str(user.user_id),
                "username": user.username,
                "user_email": user.user_email,
                "user_password": user.user_password,
                "full_name": user.full_name,
                "bio": user.bio,
                "social_links": user.social_links,
                "profile_image_url": user.profile_image_url,
            }
        )

    def get_by_id(self, user_id: UserId) -> Optional[User]:
        user = self.__users.find_one({"user_id": str(user_id.value)})
        if not user:
            return None
        return self._get_user_from_result(user)

    def get_by_username(self, username: Username) -> Optional[User]:
        user = self.__users.find_one({"username": username.value})
        if not user:
            return None
        return self._get_user_from_result(user)

    def get_by_email(self, user_email: UserEmail) -> Optional[User]:
        user = self.__users.find_one({"user_email": user_email.value})
        if not user:
            return None
        return self._get_user_from_result(user)

    def update_user_profile(self, user: User) -> None:
        self.__users.update_one(
            {"user_id": str(user.user_id)},
            {
                "$set": {
                    "full_name": user.full_name,
                    "bio": user.bio,
                    "social_links": user.social_links,
                    "profile_image_url": user.profile_image_url,
                }
            },
        )

    def _get_user_from_result(self, result: dict) -> User:
        return User(
            user_id=UserId.from_string(result["user_id"]),
            username=Username.from_string(result["username"]),
            user_email=UserEmail.from_string(result["user_email"]),
            user_password=UserPassword.from_hash(result["user_password"]),
            full_name=FullName.from_string(result["full_name"]),
            bio=UserBio.from_string(result["bio"]) if result["bio"] else None,
            social_links=SocialLinks.from_dict(
                result["social_links"] if result["social_links"] else {}
            ),
            profile_image_url=ProfileImageUrl.from_string(result["profile_image_url"]),
        )
