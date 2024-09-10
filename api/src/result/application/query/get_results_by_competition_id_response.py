from typing import List, Optional

from ..result_dto import ResultDTO


class GetResultsByCompetitionIdResponse:

    def __init__(self, results: Optional[List[ResultDTO]] = None):
        self.__results = results if results is not None else []

    @property
    def results(self) -> List[ResultDTO]:
        return self.__results

    def add_result(self, result: ResultDTO) -> List[ResultDTO] | None:
        self.__results.append(result)
