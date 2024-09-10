from ...domain.model.competition import CompetitionId
from ...domain.repository.competitions import Competitions
from .get_competition_response import GetCompetitionResponse


class GetCompetitionByIdQuery:
    def __init__(self, competition_id: str):
        self.__competition_id: str = competition_id

    @property
    def competition_id(self):
        return self.__competition_id


class GetCompetitionByIdHandler:
    def __init__(self, competitions: Competitions):
        self.__competitions: Competitions = competitions

    def handle(self, query: GetCompetitionByIdQuery):
        competition_id = CompetitionId.from_string(query.competition_id)

        competition = self.__competitions.get_by_id(competition_id)

        if not competition:
            return None

        return GetCompetitionResponse(
            competition_id=str(competition.competition_id),
            organizer_id=str(competition.organizer_id),
            name=competition.name,
            description=competition.description,
            date=competition.date.__str__,
            location=competition.location,
            image=competition.image,
            participant_limit=competition.participant_limit,
            penalty_time=competition.penalty_time,
            status=competition.status,
        )
