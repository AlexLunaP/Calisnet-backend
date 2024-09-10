from typing import Optional

import bcrypt
from dependency_injector.wiring import Provide, inject

from ...application.command.create_user import CreateUser
from ...application.command.update_user_profile import UpdateUserProfile
from ...application.query.get_user_by_email import (
    GetUserByEmailHandler,
    GetUserByEmailQuery,
)
from ...application.query.get_user_by_id import GetUserByIdHandler, GetUserByIdQuery
from ...application.query.get_user_by_username import (
    GetUserByUsernameHandler,
    GetUserByUsernameQuery,
)
from ...application.query.get_user_response import GetUserResponse
from ...domain.exceptions.incorrect_password import IncorrectPassword
from ...domain.exceptions.user_was_not_found import UserWasNotFound
from ...domain.repository.users import Users


class UserService:

    @inject
    def __init__(self, users: Users = Provide["USERS"]):
        self.users: Users = users
        self.create_user_command = CreateUser(users)
        self.update_user_profile_command = UpdateUserProfile(users)
        self.get_user_by_id_handler = GetUserByIdHandler(users)
        self.get_user_by_email_handler = GetUserByEmailHandler(users)
        self.get_user_by_username_handler = GetUserByUsernameHandler(users)

    def create_user(self, user_dto: dict):
        user_id = user_dto["userId"]
        username = user_dto["username"]
        user_email = user_dto["userEmail"]
        user_password = user_dto["userPassword"]

        self.create_user_command.handle(user_id, username, user_email, user_password)

    def get_user(self, user_id: str):
        user = self.get_user_by_id_handler.handle(GetUserByIdQuery(user_id))

        if not user:
            return None

        return user.user_dto

    def get_user_by_username(self, username: str):
        user = self.get_user_by_username_handler.handle(
            GetUserByUsernameQuery(username)
        )

        if not user:
            return None

        return user.user_dto

    def login_user(self, user_email: str, user_password: str):
        user: Optional[GetUserResponse] = self.get_user_by_email_handler.handle(
            GetUserByEmailQuery(user_email)
        )

        if not user:
            raise UserWasNotFound(f"User with email {user_email} was not found")

        if not bcrypt.checkpw(
            user_password.encode("utf-8"), user.user_password.encode("utf-8")
        ):
            raise IncorrectPassword(
                f"Incorrect password for user with email {user_email}"
            )

        return user.user_dto

    def update_user_profile(
        self,
        user_id: str,
        full_name: str,
        bio: str,
        social_links: dict,
        profile_image_url: str,
    ):
        user = self.get_user_by_id_handler.handle(GetUserByIdQuery(user_id))

        if not user:
            raise UserWasNotFound(f"User with ID {user_id} was not found")

        self.update_user_profile_command.handle(
            user_id, full_name, bio, social_links, profile_image_url
        )
