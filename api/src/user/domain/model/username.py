class Username:

    class InvalidUserName(Exception):
        pass

    def __init__(self, username: str):
        self.__validateUsernameNotEmpty(username)
        self.__validateUsernameSpacing(username)
        self.__username: str = username

    @staticmethod
    def fromString(username: str):
        return Username(username)

    @property
    def value(self):
        return self.__username

    def __validateUsernameNotEmpty(self, username: str):
        if len(username) == 0:
            raise self.InvalidUserName("Username cannot be empty")

    def __validateUsernameSpacing(self, username: str):
        if " " in username:
            raise self.InvalidUserName("Username cannot have white spaces")
