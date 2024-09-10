from typing import List, Optional

from ....shared.domain.competition_id import CompetitionId
from ...application.result_dto import ResultDTO
from ...domain.repository.results import Results
from .get_results_by_competition_id_response import GetResultsByCompetitionIdResponse


class GetResultsByCompetitionIdQuery:
    def __init__(self, competition_id: str):
        self.__competition_id: str = competition_id

    @property
    def competition_id(self):
        return self.__competition_id


class GetResultsByCompetitionIdHandler:
    def __init__(self, results: Results):
        self.__results = results

    def handle(
        self, query: GetResultsByCompetitionIdQuery
    ) -> Optional[GetResultsByCompetitionIdResponse]:
        competition_id = CompetitionId.from_string(query.competition_id)

        results: List[ResultDTO] | None = self.__results.get_by_competition_id(
            competition_id
        )

        if not results:
            return None

        get_results_by_competition_id_response = GetResultsByCompetitionIdResponse(
            results
        )

        return get_results_by_competition_id_response
