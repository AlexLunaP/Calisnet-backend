from abc import ABC, abstractmethod
from typing import Optional

from ....shared.domain.user_id import UserId
from ..model.user import User
from ..model.user_email import UserEmail
from ..model.username import Username


class Users(ABC):

    @abstractmethod
    def save(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    def getById(self, userId: UserId) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def getByUsername(self, username: Username) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def getByEmail(self, userEmail: UserEmail) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def updateUserProfile(self, user: User) -> None:
        raise NotImplementedError
