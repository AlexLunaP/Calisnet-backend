from typing import Optional


class GetUserResponse:
    def __init__(
        self,
        userId: str,
        username: str,
        userEmail: str,
        userPassword: str,
        bio: Optional[str] = None,
        birthdate: Optional[str] = None,
        profilePicUrl: Optional[str] = None,
        socialLinks: Optional[dict] = None,
        competitionHistory: Optional[list] = None,
        achievements: Optional[list] = None,
    ):
        self.__userId: str = userId
        self.__username: str = username
        self.__userEmail: str = userEmail
        self.__userPassword: str = userPassword
        self.__bio: Optional[str] = bio if bio is not None else ""
        self.__birthdate: Optional[str] = birthdate
        self.__profilePicUrl: Optional[str] = profilePicUrl
        self.__socialLinks: Optional[dict] = (
            socialLinks if socialLinks is not None else {}
        )
        self.__competitionHistory: Optional[list] = (
            competitionHistory if competitionHistory is not None else []
        )
        self.__achievements: Optional[list] = (
            achievements if achievements is not None else []
        )

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
    def bio(self):
        return self.__bio

    @property
    def birthdate(self):
        return self.__birthdate

    @property
    def profilePicUrl(self):
        return self.__profilePicUrl

    @property
    def socialLinks(self):
        return self.__socialLinks

    @property
    def competitionHistory(self):
        return self.__competitionHistory

    @property
    def achievements(self):
        return self.__achievements

    @property
    def userDto(self):
        return {
            "userId": self.__userId,
            "username": self.__username,
            "userEmail": self.__userEmail,
            "userPassword": self.__userPassword,
            "bio": self.__bio,
            "birthdate": self.__birthdate,
            "profilePicUrl": self.__profilePicUrl,
            "socialLinks": self.__socialLinks,
            "competitionHistory": self.__competitionHistory,
            "achievements": self.__achievements,
        }
