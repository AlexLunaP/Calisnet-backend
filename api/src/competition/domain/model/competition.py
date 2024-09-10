from typing import Optional

from ....shared.domain.competition_id import CompetitionId
from ....user.domain.model.user import UserId
from .competition_date import CompetitionDate
from .competition_description import CompetitionDescription
from .competition_image_url import CompetitionImageUrl
from .competition_location import CompetitionLocation
from .competition_name import CompetitionName
from .competition_status import CompetitionStatus
from .participant_limit import ParticipantLimit
from .penalty_time import PenaltyTime


class Competition:

    def __init__(
        self,
        competition_id: CompetitionId,
        organizer_id: UserId,
        name: CompetitionName,
        description: CompetitionDescription,
        date: CompetitionDate,
        location: CompetitionLocation,
        image: CompetitionImageUrl,
        participant_limit: Optional[ParticipantLimit],
        penalty_time: PenaltyTime,
        status: CompetitionStatus = CompetitionStatus.OPEN,
    ):
        self._competition_id: CompetitionId = competition_id
        self._organizer_id: UserId = organizer_id
        self._name: CompetitionName = name
        self._description: CompetitionDescription = description
        self._date: CompetitionDate = date
        self._location: CompetitionLocation = location
        self._image: CompetitionImageUrl = image
        self._participant_limit: ParticipantLimit = (
            participant_limit if participant_limit else ParticipantLimit(0)
        )
        self._penalty_time: PenaltyTime = penalty_time
        self._status: CompetitionStatus = status

    @property
    def competition_id(self):
        return self._competition_id.value

    @property
    def organizer_id(self):
        return self._organizer_id.value

    @property
    def name(self):
        return self._name.value

    @property
    def description(self):
        return self._description.value

    @property
    def date(self):
        return self._date

    @property
    def location(self):
        return self._location.value

    @property
    def image(self):
        return self._image.value

    @property
    def participant_limit(self):
        return self._participant_limit.value

    @property
    def penalty_time(self):
        return self._penalty_time.value

    @property
    def status(self):
        return self._status.value

    @classmethod
    def add(
        cls,
        competition_id: CompetitionId,
        organizer_id: UserId,
        name: CompetitionName,
        description: CompetitionDescription,
        date: CompetitionDate,
        location: CompetitionLocation,
        image: CompetitionImageUrl,
        participant_limit: Optional[ParticipantLimit],
        penalty_time: PenaltyTime,
        status: CompetitionStatus,
    ) -> "Competition":
        return cls(
            competition_id=competition_id,
            organizer_id=organizer_id,
            name=name,
            description=description,
            date=date,
            location=location,
            image=image,
            participant_limit=participant_limit,
            penalty_time=penalty_time,
            status=status,
        )

    def update_name(self, name: CompetitionName):
        self._name = name

    def update_description(self, description: CompetitionDescription):
        self._description = description

    def update_date(self, date: CompetitionDate):
        self._date = date

    def update_location(self, location: CompetitionLocation):
        self._location = location

    def update_image(self, image: CompetitionImageUrl):
        self._image = image

    def update_participant_limit(self, participant_limit: ParticipantLimit):
        self._participant_limit = participant_limit

    def update_penalty_time(self, penalty_time: PenaltyTime):
        self._penalty_time = penalty_time

    def update_status(self, status: CompetitionStatus):
        self._status = status
