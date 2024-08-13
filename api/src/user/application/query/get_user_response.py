class GetUserResponse:
    def __init__(self, userId: str, username: str, userEmail: str, userPassword: str):
        self.__userId: str = userId
        self.__username: str = username
        self.__userEmail: str = userEmail
        self.__userPassword: str = userPassword

    @property
    def userId(self):
        return self.__userId

    @property
    def username(self):
        return self.__username

    @property
    def userEmail(self):
        return self.__userEmail

    @property
    def userPassword(self):
        return self.__userPassword

    @property
    def userDto(self):
        return {
            "userId": self.__userId,
            "username": self.__username,
            "userEmail": self.__userEmail,
            "userPassword": self.__userPassword,
        }
