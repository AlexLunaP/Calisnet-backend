from typing import Optional

from ...application.query.get_user_response import GetUserResponse
from ...domain.model.user_email import UserEmail
from ...domain.repository.users import Users


class GetUserByEmailQuery:

    def __init__(self, userEmail: str):
        self.__userEmail: str = userEmail

    @property
    def userEmail(self):
        return self.__userEmail


class GetUserByEmailHandler:

    def __init__(self, users: Users):
        self.__users: Users = users

    def handle(self, query: GetUserByEmailQuery):
        userEmail = UserEmail.fromString(query.userEmail)

        user = self.__users.getByEmail(userEmail)

        if not user:
            return None

        return GetUserResponse(
            userId=str(user.userId),
            username=user.username,
            userEmail=user.userEmail,
            userPassword=user.userPassword.decode("utf-8"),
        )
