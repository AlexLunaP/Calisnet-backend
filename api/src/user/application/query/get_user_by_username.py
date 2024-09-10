from ....shared.infrastructure.media_utils import get_base64_image
from ...application.query.get_user_response import GetUserResponse
from ...domain.model.username import Username
from ...domain.repository.users import Users


class GetUserByUsernameQuery:

    def __init__(self, username: str):
        self.username: str = username

    @property
    def get_username(self):
        return self.username


class GetUserByUsernameHandler:

    def __init__(self, users: Users):
        self.users: Users = users

    def handle(self, query: GetUserByUsernameQuery):
        username = Username.from_string(query.get_username)

        user = self.users.get_by_username(username)

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
