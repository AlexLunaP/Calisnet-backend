from ....shared.domain.user_id import UserId
from .user_email import UserEmail
from .user_password import UserPassword
from .username import Username


class User:

    def __init__(
        self,
        userId: UserId,
        username: Username,
        userEmail: UserEmail,
        userPassword: UserPassword,
    ):
        self._userId = userId
        self._username = username
        self._userEmail = userEmail
        self._password = userPassword

    @property
    def userId(self):
        return self._userId.value

    @property
    def username(self):
        return self._username.value

    @property
    def userEmail(self):
        return self._userEmail.value

    @property
    def userPassword(self):
        return self._password.value
