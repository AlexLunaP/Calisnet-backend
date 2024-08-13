import re


class UserEmail:

    class InvalidEmail(Exception):
        pass

    def __init__(self, userEmail: str):
        self.validateEmail(userEmail)
        self.__value = userEmail

    @staticmethod
    def fromString(userEmail: str):
        return UserEmail(userEmail)

    @property
    def value(self):
        return self.__value

    def validateEmail(self, userEmail):
        if not re.fullmatch(
            r"^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$", userEmail
        ):
            raise self.InvalidEmail("Email format is not valid")
