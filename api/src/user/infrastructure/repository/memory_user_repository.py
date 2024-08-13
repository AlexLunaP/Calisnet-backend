from typing import List, Optional

from ....shared.domain.user_id import UserId
from ...domain.model.user import User
from ...domain.model.user_email import UserEmail
from ...domain.model.username import Username
from ...domain.repository.users import Users


class MemoryUserRepository(Users):
    def __init__(self):
        self.__users: List[User] = []

    def save(self, user: User) -> None:
        self.__users.append(user)

    def getById(self, userId: UserId) -> Optional[User]:
        for user in self.__users:
            if user.userId == userId.value:
                return user

    def getByUsername(self, username: Username) -> Optional[User]:
        for user in self.__users:
            if user.username == username.value:
                return user

    def getByEmail(self, userEmail: UserEmail) -> Optional[User]:
        for user in self.__users:
            if user.userEmail == userEmail.value:
                return user
