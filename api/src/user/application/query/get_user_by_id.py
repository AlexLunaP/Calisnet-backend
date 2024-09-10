from ....shared.domain.user_id import UserId
from ....shared.infrastructure.media_utils import get_base64_image
from ...application.query.get_user_response import GetUserResponse
from ...domain.repository.users import Users


class GetUserByIdQuery:

    def __init__(self, user_id: str):
        self.__user_id: str = user_id

    @property
    def user_id(self):
        return self.__user_id


class GetUserByIdHandler:

    def __init__(self, users: Users):
        self.__users: Users = users

    def handle(self, query: GetUserByIdQuery):
        user_id = UserId.from_string(query.user_id)

        user = self.__users.get_by_id(user_id)

        if not user:
            return None

        if user.profile_image_url is not None:
            profile_image_base64 = get_base64_image(user.profile_image_url)
        else:
            profile_image_base64 = None

        return GetUserResponse(
            user_id=str(user.user_id),
            username=user.username,
            user_email=user.user_email,
            user_password=user.user_password.decode("utf-8"),
            full_name=user.full_name,
            bio=user.bio,
            social_links=user.social_links,
            profile_image_url=profile_image_base64,
        )
