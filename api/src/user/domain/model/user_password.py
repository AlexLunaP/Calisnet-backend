import bcrypt


class UserPassword:

    def __init__(self, password: str):
        self.__value = self.__hash_password(password)

    def __hash_password(self, password: str) -> bytes:
        salt = bcrypt.gensalt()
        hashedPassword = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashedPassword

    @staticmethod
    def fromString(password: str):
        return UserPassword(password)

    @staticmethod
    def fromHash(hashedPassword: bytes):
        userPassword = UserPassword("")
        userPassword.__value = hashedPassword
        return userPassword

    @property
    def value(self):
        return self.__value
