from typing import List, Optional

from ....shared.domain.user_id import UserId
from ...application.competition_dto import CompetitionDTO
from ...domain.repository.competitions import Competitions
from .get_competitions_by_organizer_id_response import (
    GetCompetitionsByOrganizerIdResponse,
)


class GetCompetitionsByOrganizerIdQuery:
    def __init__(self, organizer_id: str):
        self.__organizer_id: str = organizer_id

    @property
    def organizer_id(self):
        return self.__organizer_id


class GetCompetitionsByOrganizerIdHandler:
    def __init__(self, competitions: Competitions):
        self.__competitions = competitions

    def handle(
        self, query: GetCompetitionsByOrganizerIdQuery
    ) -> Optional[GetCompetitionsByOrganizerIdResponse]:
        organizer_id = UserId.from_string(query.organizer_id)

        competitions: List[CompetitionDTO] | None = (
            self.__competitions.get_by_organizer_id(organizer_id)
        )

        if not competitions:
            return None

        get_competitions_by_organizer_id_response = (
            GetCompetitionsByOrganizerIdResponse(competitions)
        )

        return get_competitions_by_organizer_id_response
