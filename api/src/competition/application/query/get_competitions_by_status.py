from typing import List, Optional

from ...application.competition_dto import CompetitionDTO
from ...domain.model.competition_status import CompetitionStatus
from ...domain.repository.competitions import Competitions
from .get_competitions_by_status_response import GetCompetitionsByStatusResponse


class GetCompetitionsByStatusQuery:
    def __init__(self, status: str):
        self.__status: str = status

    @property
    def status(self):
        return self.__status


class GetCompetitionsByStatusHandler:
    def __init__(self, competitions: Competitions):
        self.__competitions = competitions

    def handle(
        self, query: GetCompetitionsByStatusQuery
    ) -> Optional[GetCompetitionsByStatusResponse]:
        status = CompetitionStatus.from_string(query.status)

        competitions: List[CompetitionDTO] | None = self.__competitions.get_by_status(
            status
        )

        if not competitions:
            return None

        get_competitions_by_status_response = GetCompetitionsByStatusResponse(
            competitions
        )

        return get_competitions_by_status_response
