from typing import Optional
from uuid import uuid4

from dependency_injector.wiring import Provide, inject

from ...application.command.create_result import CreateResult
from ...application.command.update_result import UpdateResult
from ...application.query.get_result_by_id import (
    GetResultByIdHandler,
    GetResultByIdQuery,
)
from ...application.query.get_results_by_competition_id import (
    GetResultsByCompetitionIdHandler,
    GetResultsByCompetitionIdQuery,
)
from ...application.query.get_results_by_participant_id import (
    GetResultsByParticipantIdHandler,
    GetResultsByParticipantIdQuery,
)
from ...application.result_dto import ResultDTO
from ...domain.repository.results import Results


class ResultService:

    @inject
    def __init__(self, results: Results = Provide["RESULTS"]):
        self.results: Results = results
        self.create_result_command = CreateResult(results)
        self.get_result_by_id_handler = GetResultByIdHandler(results)
        self.get_results_by_competition_id_handler = GetResultsByCompetitionIdHandler(
            results
        )
        self.get_results_by_participant_id_handler = GetResultsByParticipantIdHandler(
            results
        )
        self.update_result_command = UpdateResult(results)

    def create_result(self, result_dto: ResultDTO):
        result_id = str(uuid4())
        competition_id = result_dto["competition_id"]
        participant_id = result_dto["participant_id"]
        result_time = result_dto["result_time"]
        penalties = result_dto["penalties"]
        rank = result_dto["rank"]

        self.create_result_command.handle(
            result_id,
            competition_id,
            participant_id,
            result_time,
            penalties,
            rank,
        )

    def get_result(self, result_id: str):
        result = self.get_result_by_id_handler.handle(GetResultByIdQuery(result_id))

        if not result:
            return None

        return result.result_dto

    def get_results(
        self,
        competition_id: Optional[str] = None,
        participant_id: Optional[str] = None,
    ):
        results = None

        if competition_id:
            results = self.get_results_by_competition_id_handler.handle(
                GetResultsByCompetitionIdQuery(competition_id)
            )

        elif participant_id:
            results = self.get_results_by_participant_id_handler.handle(
                GetResultsByParticipantIdQuery(participant_id)
            )

        if not results:
            return None

        return results.results

    def update_result(self, result_dto: ResultDTO):
        result_id = result_dto["result_id"]
        competition_id = result_dto["competition_id"]
        participant_id = result_dto["participant_id"]
        result_time = result_dto["result_time"]
        penalties = result_dto["penalties"]
        rank = result_dto["rank"]

        self.update_result_command.handle(
            result_id,
            competition_id,
            participant_id,
            int(result_time),
            int(penalties),
            int(rank),
        )
