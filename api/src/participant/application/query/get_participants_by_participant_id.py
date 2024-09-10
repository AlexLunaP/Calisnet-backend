from typing import List, Optional

from ...application.participant_dto import ParticipantDTO
from ...domain.model.participant_id import ParticipantId
from ...domain.repository.participants import Participants
from .get_participants_by_participant_id_response import (
    GetParticipantsByParticipantIdResponse,
)


class GetParticipantsByParticipantIdQuery:
    def __init__(self, participant_id: str):
        self.__participant_id: str = participant_id

    @property
    def participant_id(self):
        return self.__participant_id


class GetParticipantsByParticipantIdHandler:
    def __init__(self, participants: Participants):
        self.__participants = participants

    def handle(
        self, query: GetParticipantsByParticipantIdQuery
    ) -> Optional[GetParticipantsByParticipantIdResponse]:
        participant_id = ParticipantId.from_string(query.participant_id)

        participants: List[ParticipantDTO] | None = (
            self.__participants.get_by_participant_id(participant_id)
        )

        if not participants:
            return None

        get_participants_by_competition_id_response = (
            GetParticipantsByParticipantIdResponse(participants)
        )

        return get_participants_by_competition_id_response
