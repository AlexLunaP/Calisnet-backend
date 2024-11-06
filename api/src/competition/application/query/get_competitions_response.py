from typing import List, Optional

from ...application.competition_dto import CompetitionDTO


class GetCompetitionsResponse:

    def __init__(self, competitions: Optional[List[CompetitionDTO]] = None):
        self.__competitions = competitions if competitions is not None else []

    @property
    def competitions(self) -> List[CompetitionDTO]:
        return self.__competitions

    def add_competition(
        self, competition: CompetitionDTO
    ) -> List[CompetitionDTO] | None:
        self.__competitions.append(competition)
