from typing import List, Optional

from ....shared.domain.competition_id import CompetitionId
from ...application.participant_dto import ParticipantDTO
from ...domain.repository.participants import Participants
from ..query.get_participants_by_competition_id_response import (
    GetParticipantsByCompetitionIdResponse,
)


class GetParticipantsByCompetitionIdQuery:
    def __init__(self, competition_id: str):
        self.__competition_id: str = competition_id

    @property
    def competition_id(self):
        return self.__competition_id


class GetParticipantsByCompetitionIdHandler:
    def __init__(self, participants: Participants):
        self.__participants = participants

    def handle(
        self, query: GetParticipantsByCompetitionIdQuery
    ) -> Optional[GetParticipantsByCompetitionIdResponse]:
        competition_id = CompetitionId.from_string(query.competition_id)

        participants: List[ParticipantDTO] | None = (
            self.__participants.get_by_competition_id(competition_id)
        )

        if not participants:
            return None

        get_participants_by_competition_id_response = (
            GetParticipantsByCompetitionIdResponse(participants)
        )

        return get_participants_by_competition_id_response
