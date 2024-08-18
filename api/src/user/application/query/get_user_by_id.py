from ....shared.domain.user_id import UserId
from ...application.query.get_user_response import GetUserResponse
from ...domain.repository.users import Users


class GetUserByIdQuery:

    def __init__(self, userId: str):
        self.__userId: str = userId

    @property
    def userId(self):
        return self.__userId


class GetUserByIdHandler:

    def __init__(self, users: Users):
        self.__users: Users = users

    def handle(self, query: GetUserByIdQuery):
        userId = UserId.fromString(query.userId)

        user = self.__users.getById(userId)

        if not user:
            return None

        return GetUserResponse(
            userId=str(user.userId),
            username=user.username,
            userEmail=user.userEmail,
            userPassword=user.userPassword.decode("utf-8"),
            bio=user.bio,
            birthdate=str(user.birthdate),
            profilePicUrl=user.profilePicUrl,
            socialLinks=user.socialLinks,
            competitionHistory=user.competitionHistory,
            achievements=user.achievements,
        )
