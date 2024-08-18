from datetime import datetime

from ....shared.domain.user_id import UserId
from ...domain.exception.user_was_not_found import UserWasNotFound
from ...domain.model.user import User
from ...domain.repository.users import Users


class UpdateUserProfile:
    def __init__(self, users: Users):
        self.users = users

    def handle(
        self,
        userId: str,
        bio: str,
        birthdate: datetime,
        profilePicUrl: str,
        socialLinks: dict,
    ):
        userIdObject = UserId.fromString(userId)
        user = self.users.getById(userIdObject)

        if not user:
            raise UserWasNotFound("The user was not found")
        user.updateBio(bio)
        user.updateBirthdate(birthdate)
        user.updateProfilePicUrl(profilePicUrl)
        user.updateSocialLinks(socialLinks)

        self.users.updateUserProfile(user)
