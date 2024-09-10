from ...application.query.get_user_response import GetUserResponse
from ...domain.model.user_email import UserEmail
from ...domain.repository.users import Users


class GetUserByEmailQuery:

    def __init__(self, user_email: str):
        self.__user_email: str = user_email

    @property
    def user_email(self):
        return self.__user_email


class GetUserByEmailHandler:

    def __init__(self, users: Users):
        self.__users: Users = users

    def handle(self, query: GetUserByEmailQuery):
        user_email = UserEmail.from_string(query.user_email)

        user = self.__users.get_by_email(user_email)

        if not user:
            return None

        return GetUserResponse(
            user_id=str(user.user_id),
            username=user.username,
            user_email=user.user_email,
            user_password=user.user_password.decode("utf-8"),
            full_name=user.full_name,
            bio=user.bio,
            social_links=user.social_links,
            profile_image_url=user.profile_image_url,
        )
