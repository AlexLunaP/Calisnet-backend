from typing import Optional

import bcrypt
from dependency_injector.wiring import Provide, inject
from flask import jsonify

from ...application.command.create_user import CreateUser
from ...application.query.get_user_by_email import (
    GetUserByEmailHandler,
    GetUserByEmailQuery,
)
from ...application.query.get_user_by_id import GetUserByIdHandler, GetUserByIdQuery
from ...application.query.get_user_response import GetUserResponse
from ...domain.exception.incorrect_password import IncorrectPassword
from ...domain.exception.user_was_not_found import UserWasNotFound
from ...domain.model.user_password import UserPassword
from ...domain.repository.users import Users
from ...infrastructure.user_providers import UserProviders


class UserService:

    @inject
    def __init__(self, users: Users = Provide["USERS"]):
        self.users: Users = users
        self.createUserCommand = CreateUser(users)
        self.getUserByIdHandler = GetUserByIdHandler(users)
        self.getUserByEmailHandler = GetUserByEmailHandler(users)

    def createUser(self, userDto: dict):
        userId = userDto["userId"]
        username = userDto["username"]
        userEmail = userDto["userEmail"]
        userPassword = userDto["userPassword"]

        self.createUserCommand.handle(userId, username, userEmail, userPassword)

    def getUser(self, userId: str):
        user = self.getUserByIdHandler.handle(GetUserByIdQuery(userId))

        if not user:
            return None

        return user.userDto

    def loginUser(self, userEmail: str, userPassword: str):
        user: Optional[GetUserResponse] = self.getUserByEmailHandler.handle(
            GetUserByEmailQuery(userEmail)
        )

        if not user:
            raise UserWasNotFound(f"User with email {userEmail} was not found")

        if not bcrypt.checkpw(
            userPassword.encode("utf-8"), user.userPassword.encode("utf-8")
        ):
            raise IncorrectPassword(
                f"Incorrect password for user with email {userEmail}"
            )

        return user.userDto
