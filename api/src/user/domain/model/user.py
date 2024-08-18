from datetime import datetime
from typing import Dict, List, Optional

from ....shared.domain.user_id import UserId
from .achievement import Achievement
from .competition_history_entry import CompetitionHistoryEntry
from .user_email import UserEmail
from .user_password import UserPassword
from .username import Username


class User:

    def __init__(
        self,
        userId: UserId,
        username: Username,
        userEmail: UserEmail,
        userPassword: UserPassword,
        bio: Optional[str] = None,
        birthdate: Optional[datetime] = None,
        profilePicUrl: Optional[str] = None,
        socialLinks: Optional[Dict[str, str]] = None,
        competitionHistory: Optional[List[CompetitionHistoryEntry]] = None,
        achievements: Optional[List[Achievement]] = None,
    ):
        self._userId: UserId = userId
        self._username: Username = username
        self._userEmail: UserEmail = userEmail
        self._password = userPassword
        self._bio: str | None = bio
        self._birthdate: datetime | None = birthdate
        self._profilePicUrl: str | None = profilePicUrl
        self._socialLinks = socialLinks
        self._competitionHistory = competitionHistory
        self._achievements = achievements

    @property
    def userId(self):
        return self._userId.value

    @property
    def username(self):
        return self._username.value

    @property
    def userEmail(self):
        return self._userEmail.value

    @property
    def userPassword(self):
        return self._password.value

    @property
    def bio(self):
        return self._bio

    @property
    def birthdate(self):
        return self._birthdate

    @property
    def profilePicUrl(self):
        return self._profilePicUrl

    @property
    def socialLinks(self):
        return self._socialLinks

    @property
    def competitionHistory(self):
        return self._competitionHistory

    @property
    def achievements(self):
        return self._achievements

    def updateBio(self, bio: Optional[str]):
        self._bio = bio

    def updateBirthdate(self, birthdate: Optional[datetime]):
        self._birthdate = birthdate

    def updateProfilePicUrl(self, profilePicUrl: Optional[str]):
        self._profilePicUrl = profilePicUrl

    def updateSocialLinks(self, socialLinks: Optional[Dict[str, str]]):
        self._socialLinks = socialLinks

    def updateCompetitionHistory(
        self, competitionHistory: Optional[List[CompetitionHistoryEntry]]
    ):
        self._competitionHistory = competitionHistory
