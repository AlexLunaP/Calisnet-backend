import os
from typing import List, Optional

import pymongo

from ....shared.domain.competition_id import CompetitionId
from ....shared.domain.user_id import UserId
from ...application.result_dto import ResultDTO
from ...domain.model.penalties import Penalties
from ...domain.model.rank import Rank
from ...domain.model.result import Result
from ...domain.model.result_id import ResultId
from ...domain.model.result_time import ResultTime
from ...domain.repository.results import Results


class MongoResultRepository(Results):
    def __init__(self):
        self.__db = pymongo.MongoClient(os.environ["MONGODB_URL"])[
            os.environ["MONGODB_DBNAME"]
        ]
        self.__results = self.__db["results"]

    def save(self, result) -> None:
        self.__results.insert_one(
            {
                "result_id": str(result.result_id),
                "competition_id": str(result.competition_id),
                "participant_id": str(result.participant_id),
                "result_time": str(result.result_time),
                "penalties": str(result.penalties),
                "rank": str(result.rank),
            }
        )

    def update_result(self, result: Result) -> None:
        self.__results.update_one(
            {"result_id": str(result.result_id)},
            {
                "$set": {
                    "result_time": str(result.result_time),
                    "penalties": str(result.penalties),
                    "rank": str(result.rank),
                }
            },
        )

    def get_by_id(self, result_id: ResultId) -> Optional[Result]:
        result = self.__results.find_one({"result_id": str(result_id.value)})

        if not result:
            return None

        return self._get_result_from_result(result)

    def get_by_competition_id(
        self, competition_id: CompetitionId
    ) -> List[ResultDTO] | None:

        results = self.__results.find({"competition_id": str(competition_id.value)})

        if not results:
            return None

        result_list: List[ResultDTO] = []

        for result in results:
            result_list.append(
                ResultDTO(
                    result_id=result["result_id"],
                    competition_id=result["competition_id"],
                    participant_id=result["participant_id"],
                    result_time=result["result_time"],
                    penalties=result["penalties"],
                    rank=result["rank"],
                )
            )
        return result_list

    def get_by_participant_id(self, participant_id: UserId) -> List[ResultDTO] | None:

        results = self.__results.find({"participant_id": str(participant_id.value)})

        if not results:
            return None

        result_list: List[ResultDTO] = []

        for result in results:
            result_list.append(
                ResultDTO(
                    result_id=result["result_id"],
                    competition_id=result["competition_id"],
                    participant_id=result["participant_id"],
                    result_time=result["result_time"],
                    penalties=result["penalties"],
                    rank=result["rank"],
                )
            )
        return result_list

    def _get_result_from_result(self, result) -> Result:
        return Result(
            result_id=ResultId.from_string(result["result_id"]),
            competition_id=CompetitionId.from_string(result["competition_id"]),
            participant_id=UserId.from_string(result["participant_id"]),
            result_time=ResultTime.from_string(result["result_time"]),
            penalties=Penalties.from_string(result["penalties"]),
            rank=Rank.from_string(result["rank"]),
        )
