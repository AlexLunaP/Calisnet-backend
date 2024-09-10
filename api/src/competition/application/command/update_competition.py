from ....shared.domain.competition_id import CompetitionId
from ...domain.exceptions.competition_was_not_found import CompetitionWasNotFound
from ...domain.model.competition_date import CompetitionDate
from ...domain.model.competition_description import CompetitionDescription
from ...domain.model.competition_image_url import CompetitionImageUrl
from ...domain.model.competition_location import CompetitionLocation
from ...domain.model.competition_name import CompetitionName
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
        competition = self.competitions.get_by_id(competition_id_object)

        if not competition:
            raise CompetitionWasNotFound("The competition was not found")

        if name:
            competition.update_name(CompetitionName.from_string(name))
        if description:
            competition.update_description(
                CompetitionDescription.from_string(description)
            )
        if date:
            competition.update_date(CompetitionDate.from_string(date))
        if location:
            competition.update_location(CompetitionLocation.from_string(location))
        if image:
            competition.update_image(CompetitionImageUrl.from_string(image))
        if participant_limit is not None:
            competition.update_participant_limit(ParticipantLimit(participant_limit))
        if penalty_time is not None:
            competition.update_penalty_time(PenaltyTime(penalty_time))
        if status:
            competition.update_status(CompetitionStatus.from_string(status))

        self.competitions.update_competition(competition)

        self.competitions.update_competition(competition)
