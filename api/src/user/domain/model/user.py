from typing import Optional

from ....shared.domain.user_id import UserId
from .full_name import FullName
from .profile_image_url import ProfileImageUrl
from .social_links import SocialLinks
from .user_bio import UserBio
from .user_email import UserEmail
from .user_password import UserPassword
from .username import Username


class User:

    def __init__(
        self,
        user_id: UserId,
        username: Username,
        user_email: UserEmail,
        user_password: UserPassword,
        full_name: FullName,
        bio: Optional[UserBio] = None,
        social_links: Optional[SocialLinks] = None,
        profile_image_url: Optional[ProfileImageUrl] = None,
    ):
        self._user_id: UserId = user_id
        self._username: Username = username
        self._user_email: UserEmail = user_email
        self._password = user_password
        self._full_name: FullName = full_name
        self._bio: UserBio | None = bio
        self._social_links: SocialLinks | None = social_links
        self._profile_image_url: ProfileImageUrl | None = profile_image_url

    @property
    def user_id(self):
        return self._user_id.value

    @property
    def username(self):
        return self._username.value

    @property
    def user_email(self):
        return self._user_email.value

    @property
    def user_password(self):
        return self._password.value

    @property
    def full_name(self):
        return self._full_name.value

    @property
    def bio(self):
        return self._bio.value if self._bio else None

    @property
    def social_links(self):
        return self._social_links.to_dict() if self._social_links else None

    @property
    def profile_image_url(self):
        return self._profile_image_url.value if self._profile_image_url else None

    @classmethod
    def add(
        cls,
        user_id: UserId,
        username: Username,
        user_email: UserEmail,
        user_password: UserPassword,
        full_name: FullName,
    ) -> "User":
        return cls(
            user_id=user_id,
            username=username,
            user_email=user_email,
            user_password=user_password,
            full_name=full_name,
        )

    def update_full_name(self, full_name: FullName):
        self._full_name = full_name

    def update_bio(self, bio: Optional[UserBio]):
        self._bio = bio

    def update_social_links(self, social_links: Optional[SocialLinks]):
        self._social_links = social_links

    def update_profile_image_url(self, profile_image_url: Optional[ProfileImageUrl]):
        self._profile_image_url = profile_image_url
