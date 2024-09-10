from abc import ABC, abstractmethod
from typing import List, Optional

from ....shared.domain.competition_id import CompetitionId
from ....shared.domain.user_id import UserId
from ...application.competition_dto import CompetitionDTO
from ..model.competition import Competition


class Competitions(ABC):

    @abstractmethod
    def save(self, competition: Competition) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, competition_id: CompetitionId) -> Optional[Competition]:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> Optional[List[CompetitionDTO]]:
        raise NotImplementedError

    @abstractmethod
    def get_by_status(self, competition_status: str) -> Optional[List[CompetitionDTO]]:
        raise NotImplementedError

    @abstractmethod
    def get_by_organizer_id(
        self, organizer_id: UserId
    ) -> Optional[List[CompetitionDTO]]:
        raise NotImplementedError

    @abstractmethod
    def update_competition(self, competition: Competition) -> None:
        raise NotImplementedError
