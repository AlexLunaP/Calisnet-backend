import bcrypt


class UserPassword:

    def __init__(self, password: str):
        self.__value = self.__hash_password(password)

    def __hash_password(self, password: str) -> bytes:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed_password

    @staticmethod
    def from_string(password: str):
        return UserPassword(password)

    @staticmethod
    def from_hash(hashed_password: bytes):
        user_password = UserPassword("")
        user_password.__value = hashed_password
        return user_password

    @property
    def value(self):
        return self.__value
