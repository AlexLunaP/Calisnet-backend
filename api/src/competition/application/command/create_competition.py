from ....shared.domain.competition_id import CompetitionId
from ....shared.domain.user_id import UserId
from ...domain.exceptions.competition_id_already_exists import (
    CompetitionIdAlreadyExists,
)
from ...domain.model.competition import Competition
from ...domain.model.competition_date import CompetitionDate
from ...domain.model.competition_description import CompetitionDescription
from ...domain.model.competition_image_url import CompetitionImageUrl
from ...domain.model.competition_location import CompetitionLocation
from ...domain.model.competition_name import CompetitionName
from ...domain.model.competition_status import CompetitionStatus
from ...domain.model.participant_limit import ParticipantLimit
from ...domain.model.penalty_time import PenaltyTime
from ...domain.repository.competitions import Competitions


class CreateCompetition:

    def __init__(self, competitions: Competitions):
        self.competitions = competitions

    def handle(
        self,
        competition_id: str,
        organizer_id: str,
        name: str,
        description: str,
        date: str,
        location: str,
        image: str,
        participant_limit: int,
        penalty_time: int,
        status: str,
    ):

        competition_id_object = CompetitionId.from_string(competition_id)

        if self.competitions.get_by_id(competition_id_object):
            raise CompetitionIdAlreadyExists("The competition ID already exists")

        competition = Competition.add(
            competition_id=competition_id_object,
            organizer_id=UserId.from_string(organizer_id),
            name=CompetitionName.from_string(name),
            description=CompetitionDescription.from_string(description),
            date=CompetitionDate.from_string(date),
            location=CompetitionLocation.from_string(location),
            image=CompetitionImageUrl.from_string(image),
            participant_limit=ParticipantLimit(participant_limit),
            penalty_time=PenaltyTime(penalty_time),
            status=CompetitionStatus.from_string(status),
        )

        self.competitions.save(competition)
