from ....shared.domain.user_id import UserId
from ....shared.infrastructure.media_utils import save_media
from ...domain.exceptions.user_was_not_found import UserWasNotFound
from ...domain.model.full_name import FullName
from ...domain.model.profile_image_url import ProfileImageUrl
from ...domain.model.social_links import SocialLinks
from ...domain.model.user_bio import UserBio
from ...domain.repository.users import Users


class UpdateUserProfile:
    def __init__(self, users: Users):
        self.users = users

    def handle(
        self,
        user_id: str,
        full_name: str,
        bio: str,
        social_links: dict,
        profile_image_url: str,
    ):
        user_id_object = UserId.from_string(user_id)
        user = self.users.get_by_id(user_id_object)

        if not user:
            raise UserWasNotFound("The user was not found")
        if full_name:
            user.update_full_name(FullName.from_string(full_name))
        if bio:
            user.update_bio(UserBio.from_string(bio))
        if social_links:
            user.update_social_links(SocialLinks.from_dict(social_links))
        if profile_image_url:
            image_path = save_media(profile_image_url)
            user.update_profile_image_url(ProfileImageUrl.from_string(image_path))

        self.users.update_user_profile(user)
