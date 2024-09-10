from dependency_injector.wiring import Provide, inject

from ...application.command.create_participant import CreateParticipant
from ...application.command.delete_participant import DeleteParticipant
from ...application.participant_dto import ParticipantDTO
from ...application.query.get_participants_by_competition_id import (
    GetParticipantsByCompetitionIdHandler,
    GetParticipantsByCompetitionIdQuery,
)
from ...application.query.get_participants_by_participant_id import (
    GetParticipantsByParticipantIdHandler,
    GetParticipantsByParticipantIdQuery,
)
from ...domain.repository.participants import Participants


class ParticipantService:

    @inject
    def __init__(self, participants: Participants = Provide["PARTICIPANTS"]):
        self.participants: Participants = participants
        self.create_participant_command = CreateParticipant(participants)
        self.get_participants_by_competition_id_handler = (
            GetParticipantsByCompetitionIdHandler(participants)
        )
        self.get_participants_by_participant_id_handler = (
            GetParticipantsByParticipantIdHandler(participants)
        )
        self.delete_participant_command = DeleteParticipant(participants)

    def create_participant(self, participant_dto: ParticipantDTO):
        participant_id = participant_dto["participant_id"]
        competition_id = participant_dto["competition_id"]
        name = participant_dto["name"]

        self.create_participant_command.handle(
            participant_id,
            competition_id,
            name,
        )

    def get_participants_by_competition(self, competition_id: str):
        participants = self.get_participants_by_competition_id_handler.handle(
            GetParticipantsByCompetitionIdQuery(competition_id)
        )

        if not participants:
            return None

        return participants.participants

    def get_participants_by_participant(self, participant_id: str):
        participants = self.get_participants_by_participant_id_handler.handle(
            GetParticipantsByParticipantIdQuery(participant_id)
        )

        if not participants:
            return None

        return participants.participants

    def delete_participant(self, participant_id: str, competition_id: str):
        self.delete_participant_command.handle(
            participant_id,
            competition_id,
        )
