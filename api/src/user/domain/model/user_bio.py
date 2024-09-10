class UserBio:

    MAX_BIO_LENGTH = 250

    class InvalidUserBio(Exception):
        pass

    def __init__(self, user_bio: str):
        self.__validate_user_bio_not_empty(user_bio)
        self.__validate_user_bio_length(user_bio)
        self.__user_bio: str = user_bio

    @staticmethod
    def from_string(user_bio: str):
        return UserBio(user_bio)

    @property
    def value(self):
        return self.__user_bio

    def __validate_user_bio_not_empty(self, user_bio: str):
        if len(user_bio) == 0:
            raise self.InvalidUserBio("Bio cannot be empty")

    def __validate_user_bio_length(self, user_bio: str):
        if len(user_bio) > self.MAX_BIO_LENGTH:
            raise self.InvalidUserBio(
                f"User bio cannot exceed {self.MAX_BIO_LENGTH} characters"
            )
