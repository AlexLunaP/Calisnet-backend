from abc import ABC, abstractmethod
from typing import List, Optional

from ....shared.domain.competition_id import CompetitionId
from ....shared.domain.user_id import UserId
from ...application.result_dto import ResultDTO
from ..model.result import Result
from ..model.result_id import ResultId


class Results(ABC):

    @abstractmethod
    def save(self, result: Result) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, result_id: ResultId) -> Optional[Result]:
        raise NotImplementedError

    @abstractmethod
    def get_by_competition_id(
        self, competition_id: CompetitionId
    ) -> Optional[List[ResultDTO]]:
        raise NotImplementedError

    @abstractmethod
    def get_by_participant_id(self, participantId: UserId) -> Optional[List[ResultDTO]]:
        raise NotImplementedError

    @abstractmethod
    def update_result(self, result: Result) -> None:
        raise NotImplementedError
