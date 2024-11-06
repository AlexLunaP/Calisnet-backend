from typing import List, Optional

from ...domain.repository.competitions import CompetitionDTO, Competitions
from .get_competitions_response import GetCompetitionsResponse


class GetCompetitionsHandler:
    def __init__(self, competitions: Competitions):
        self.__competitions: Competitions = competitions

    def handle(self) -> Optional[GetCompetitionsResponse]:
        competitions: List[CompetitionDTO] | None = self.__competitions.get_all()

        if not competitions:
            return None

        get_competitions_response = GetCompetitionsResponse(competitions)

        return get_competitions_response
