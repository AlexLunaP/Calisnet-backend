from abc import ABC, abstractmethod
from typing import List, Optional

from ....shared.domain.competition_id import CompetitionId
from ...application.participant_dto import ParticipantDTO
from ...domain.model.participant import Participant
from ...domain.model.participant_id import ParticipantId


class Participants(ABC):

    @abstractmethod
    def save(self, participant: Participant) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_competition_id(
        self, competition_id: CompetitionId
    ) -> Optional[List[ParticipantDTO]]:
        raise NotImplementedError

    @abstractmethod
    def get_by_participant_id(
        self, participant_id: ParticipantId
    ) -> Optional[List[ParticipantDTO]]:
        raise NotImplementedError

    @abstractmethod
    def delete_participant(self, participant: Participant) -> None:
        raise NotImplementedError
