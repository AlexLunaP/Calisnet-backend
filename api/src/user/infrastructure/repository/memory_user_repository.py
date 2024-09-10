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

    def get_by_id(self, user_id: UserId) -> Optional[User]:
        for user in self.__users:
            if user.user_id == user_id.value:
                return user

    def get_by_username(self, username: Username) -> Optional[User]:
        for user in self.__users:
            if user.username == username.value:
                return user

    def get_by_email(self, user_email: UserEmail) -> Optional[User]:
        for user in self.__users:
            if user.user_email == user_email.value:
                return user

    def update_user_profile(self, user: User) -> None:
        for i, existing_user in enumerate(self.__users):
            if existing_user.user_id == user.user_id:
                self.__users[i] = user
                break
