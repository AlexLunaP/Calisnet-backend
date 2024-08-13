from flask import logging

from ....shared.domain.user_id import UserId
from ...domain.exception.user_email_already_exists import UserEmailAlreadyExists
from ...domain.exception.user_id_already_exists import UserIdAlreadyExists
from ...domain.exception.username_already_exists import UserNameAlreadyExists
from ...domain.model.user import User
from ...domain.model.user_email import UserEmail
from ...domain.model.user_password import UserPassword
from ...domain.model.username import Username
from ...domain.repository.users import Users


class CreateUser:

    def __init__(self, users: Users):
        self.users = users

    def handle(self, userId: str, username: str, userEmail: str, userPassword: str):
        userIdObject = UserId.fromString(userId)
        usernameObject = Username.fromString(username)
        userEmailObject = UserEmail.fromString(userEmail)

        if self.users.getById(userIdObject):
            raise UserIdAlreadyExists("The user ID already exists")

        if self.users.getByUsername(usernameObject):
            raise UserNameAlreadyExists("The username already exists")

        if self.users.getByEmail(userEmailObject):
            raise UserEmailAlreadyExists("The user email already exists")

        user = User(
            userId=userIdObject,
            username=usernameObject,
            userEmail=userEmailObject,
            userPassword=UserPassword.fromString(userPassword),
        )

        self.users.save(user)
