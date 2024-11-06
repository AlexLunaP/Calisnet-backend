from typing import Optional
from uuid import uuid4

from dependency_injector.wiring import Provide, inject
from flask_jwt_extended import get_current_user
from werkzeug.exceptions import NotFound, Unauthorized

from ...application.command.create_competition import CreateCompetition
from ...application.command.update_competition import UpdateCompetition
from ...application.competition_dto import CompetitionDTO
from ...application.query.get_competition_by_id import (
    GetCompetitionByIdHandler,
    GetCompetitionByIdQuery,
)
from ...application.query.get_competitions import GetCompetitionsHandler
from ...application.query.get_competitions_by_organizer_id import (
    GetCompetitionsByOrganizerIdHandler,
    GetCompetitionsByOrganizerIdQuery,
)
from ...application.query.get_competitions_by_status import (
    GetCompetitionsByStatusHandler,
    GetCompetitionsByStatusQuery,
)
from ...domain.model.competition_status import CompetitionStatus
from ...domain.repository.competitions import Competitions


class CompetitionService:

    @inject
    def __init__(self, competitions: Competitions = Provide["COMPETITIONS"]):
        self.competitions: Competitions = competitions
        self.create_competition_command = CreateCompetition(competitions)
        self.get_competitions_handler = GetCompetitionsHandler(competitions)
        self.get_competition_by_id_handler = GetCompetitionByIdHandler(competitions)
        self.get_competitions_by_organizer_id_handler = (
            GetCompetitionsByOrganizerIdHandler(competitions)
        )
        self.get_competitions_by_status_handler = GetCompetitionsByStatusHandler(
            competitions
        )
        self.update_competition_command = UpdateCompetition(competitions)

    def create_competition(self, competition_dto: CompetitionDTO):
        competition_id = str(uuid4())
        organizer_id = competition_dto["organizer_id"]
        name = competition_dto["name"]
        description = (
            competition_dto["description"] if "description" in competition_dto else None
        )
        date = competition_dto["date"]
        location = competition_dto["location"]
        image = competition_dto["image"] if "image" in competition_dto else None
        participant_limit = competition_dto.get("participant_limit", None)
        penalty_time = (
            competition_dto["penalty_time"] if "penalty_time" in competition_dto else 0
        )
        status = CompetitionStatus.OPEN.value

        self.create_competition_command.handle(
            competition_id,
            organizer_id,
            name,
            description or "",
            date,
            location,
            image or "",
            participant_limit or 0,
            penalty_time or 0,
            status,
        )

        return competition_id

    def get_competition(self, competition_id: str):
        competition = self.get_competition_by_id_handler.handle(
            GetCompetitionByIdQuery(competition_id)
        )

        if not competition:
            return None

        return competition.competition_dto

    def get_competitions(
        self,
        organizer_id: Optional[str] = None,
        competition_status: Optional[str] = None,
    ):
        competitions = None

        if organizer_id:
            competitions = self.get_competitions_by_organizer_id_handler.handle(
                GetCompetitionsByOrganizerIdQuery(organizer_id)
            )
        elif competition_status:
            competitions = self.get_competitions_by_status_handler.handle(
                GetCompetitionsByStatusQuery(competition_status)
            )
        else:
            competitions = self.get_competitions_handler.handle()

        if not competitions:
            return None

        return competitions.competitions

    def update_competition(self, competition_dto: CompetitionDTO):
        competition_id = competition_dto["competition_id"]
        name = competition_dto["name"]
        description = competition_dto["description"]
        date = competition_dto["date"]
        location = competition_dto["location"]
        image = competition_dto["image"]
        participant_limit = competition_dto.get("participant_limit", None)
        penalty_time = competition_dto["penalty_time"]
        status = competition_dto["status"]

        competition = self.get_competition(competition_id)
        if competition is None:
            raise NotFound("Competition not found.")

        current_user_id: str = get_current_user()
        if current_user_id != competition["organizer_id"]:
            raise Unauthorized("Not allowed to modify the competition of another user.")

        self.update_competition_command.handle(
            competition_id,
            name,
            description,
            date,
            location,
            image,
            participant_limit or 0,
            penalty_time,
            status,
        )
