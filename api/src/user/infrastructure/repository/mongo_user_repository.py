import os
from typing import Optional

import pymongo

from ....shared.domain.user_id import UserId
from ...domain.model.user import User
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
                "userId": str(user.userId),
                "username": user.username,
                "userEmail": user.userEmail,
                "userPassword": user.userPassword,
            }
        )

    def getById(self, userId: UserId) -> Optional[User]:
        user = self.__users.find_one({"userId": str(userId.value)})
        if not user:
            return None
        return self.__getUserFromResult(user)

    def getByUsername(self, username: Username) -> Optional[User]:
        user = self.__users.find_one({"username": username.value})
        if not user:
            return None
        return self.__getUserFromResult(user)

    def getByEmail(self, userEmail: UserEmail) -> Optional[User]:
        user = self.__users.find_one({"userEmail": userEmail.value})
        if not user:
            return None
        return self.__getUserFromResult(user)

    def __getUserFromResult(self, result: dict) -> User:
        return User(
            userId=UserId.fromString(result["userId"]),
            username=Username.fromString(result["username"]),
            userEmail=UserEmail.fromString(result["userEmail"]),
            userPassword=UserPassword.fromHash(result["userPassword"]),
        )
