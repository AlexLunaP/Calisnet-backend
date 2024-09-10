from typing import List, Optional

from ....shared.domain.user_id import UserId
from ...application.result_dto import ResultDTO
from ...domain.repository.results import Results
from .get_results_by_participant_id_response import GetResultsByParticipantIdResponse


class GetResultsByParticipantIdQuery:
    def __init__(self, participant_id: str):
        self.__participant_id: str = participant_id

    @property
    def participant_id(self):
        return self.__participant_id


class GetResultsByParticipantIdHandler:
    def __init__(self, results: Results):
        self.__results = results

    def handle(
        self, query: GetResultsByParticipantIdQuery
    ) -> Optional[GetResultsByParticipantIdResponse]:
        participant_id = UserId.from_string(query.participant_id)

        results: List[ResultDTO] | None = self.__results.get_by_participant_id(
            participant_id
        )

        if not results:
            return None

        get_results_by_participant_id_response = GetResultsByParticipantIdResponse(
            results
        )

        return get_results_by_participant_id_response
