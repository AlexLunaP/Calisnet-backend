from datetime import datetime

from ....shared.domain.competition_id import CompetitionId
from ...domain.exceptions.competition_was_not_found import CompetitionWasNotFound
from ...domain.exceptions.invalid_competition_date import InvalidCompetitionDate
from ...domain.model.competition_date import CompetitionDate
from ...domain.model.competition_description import CompetitionDescription
from ...domain.model.competition_location import CompetitionLocation
from ...domain.model.competition_status import CompetitionStatus
from ...domain.model.participant_limit import ParticipantLimit
from ...domain.model.penalty_time import PenaltyTime
from ...domain.repository.competitions import Competitions


class UpdateCompetition:
    def __init__(self, competitions: Competitions):
        self.competitions = competitions

    def handle(
        self,
        competition_id: str,
        description: str,
        date: str,
        location: str,
        participant_limit: int,
        penalty_time: int,
        status: str,
    ):
        competition_id_object = CompetitionId.from_string(competition_id)
        competition_date_object = CompetitionDate.from_string(date)
        competition = self.competitions.get_by_id(competition_id_object)

        if not competition:
            raise CompetitionWasNotFound("The competition was not found")

        if competition_date_object.value.date() < datetime.now().date():
            raise InvalidCompetitionDate("The date cannot be in the past")

        if description:
            competition.update_description(
                CompetitionDescription.from_string(description)
            )
        if date:
            competition.update_date(competition_date_object)
        if location:
            competition.update_location(CompetitionLocation.from_string(location))
        if participant_limit is not None:
            competition.update_participant_limit(ParticipantLimit(participant_limit))
        if penalty_time is not None:
            competition.update_penalty_time(PenaltyTime(penalty_time))
        if status:
            competition.update_status(CompetitionStatus.from_string(status))

        self.competitions.update_competition(competition)
