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
    def get_by_id(self, user_id: UserId) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def get_by_username(self, username: Username) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def get_by_email(self, user_email: UserEmail) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def update_user_profile(self, user: User) -> None:
        raise NotImplementedError
