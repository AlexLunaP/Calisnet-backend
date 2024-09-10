from ...domain.model.result import ResultId
from ...domain.repository.results import Results
from .get_result_response import GetResultResponse


class GetResultByIdQuery:
    def __init__(self, result_id: str):
        self.__result_id: str = result_id

    @property
    def result_id(self):
        return self.__result_id


class GetResultByIdHandler:
    def __init__(self, results: Results):
        self.__results: Results = results

    def handle(self, query: GetResultByIdQuery):
        result_id = ResultId.from_string(query.result_id)

        result = self.__results.get_by_id(result_id)

        if not result:
            return None

        return GetResultResponse(
            result_id=str(result.result_id),
            participant_id=str(result.participant_id),
            competition_id=str(result.competition_id),
            result_time=int(result.result_time.total_seconds()),
            penalties=result.penalties,
            rank=result.rank,
        )
