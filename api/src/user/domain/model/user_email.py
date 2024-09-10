import re


class UserEmail:
    class InvalidEmail(Exception):
        pass

    def __init__(self, user_email: str):
        self.validate_email(user_email)
        self.__value = user_email

    @staticmethod
    def from_string(user_email: str):
        return UserEmail(user_email)

    @property
    def value(self):
        return self.__value

    def validate_email(self, user_email):
        if not re.fullmatch(
            r"^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$", user_email
        ):
            raise self.InvalidEmail("Email format is not valid")
