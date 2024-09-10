from typing import List, Optional

from ..participant_dto import ParticipantDTO


class GetParticipantsByCompetitionIdResponse:

    def __init__(self, participants: Optional[List[ParticipantDTO]] = None):
        self.__participants = participants if participants is not None else []

    @property
    def participants(self) -> List[ParticipantDTO]:
        return self.__participants

    def add_participant(
        self, participant: ParticipantDTO
    ) -> List[ParticipantDTO] | None:
        self.__participants.append(participant)
