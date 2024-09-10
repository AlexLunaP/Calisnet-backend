from typing import List, Optional

from ....shared.domain.competition_id import CompetitionId
from ...domain.model.competition import Competition
from ...domain.repository.competitions import Competitions


class MemoryCompetitionRepository(Competitions):
    def __init__(self):
        self.__competitions: List[Competition] = []

    def save(self, competition: Competition) -> None:
        self.__competitions.append(competition)

    def get_by_id(self, competition_id: CompetitionId) -> Optional[Competition]:
        for competition in self.__competitions:
            if competition.competition_id == competition_id.value:
                return competition
