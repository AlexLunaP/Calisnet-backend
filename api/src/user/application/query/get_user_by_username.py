from ...domain.model.username import Username
from ...domain.repository.users import Users


class GetUserByUsernameQuery:

    def __init__(self, username: str):
        self.__username: str = username

    @property
    def username(self):
        return self.__username


class GetUserByUsernameHandler:

    def __init__(self, users: Users):
        self.__users: Users = users

    def handle(self, query: GetUserByUsernameQuery):
        username = Username.fromString(query.username)

        user = self.__users.getByUsername(username)

        if not user:
            return None

        return {
            "userId": str(user.userId),
            "username": user.username,
            "userEmail": user.userEmail,
            "userPassword": user.userPassword,
            "bio": user.bio,
            "birthdate": user.birthdate,
            "profilePicUrl": user.profilePicUrl,
            "socialLinks": user.socialLinks,
            "competitionHistory": user.competitionHistory,
            "achievements": user.achievements,
        }
