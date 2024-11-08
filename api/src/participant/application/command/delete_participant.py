from ...domain.exceptions.participant_was_not_found import ParticipantWasNotFound
from ...domain.model.participant_id import ParticipantId
from ...domain.repository.participants import Participants


class DeleteParticipant:
    def __init__(self, participants: Participants):
        self.participants = participants

    def handle(
        self,
        participant_id: str,
        competition_id: str,
    ):
        participant = self.participants.get_by_participant_id(
            ParticipantId.from_string(participant_id)
        )
        if not participant:
            raise ParticipantWasNotFound("Participant not found")

        if not any(p["competition_id"] == competition_id for p in participant):
            raise ParticipantWasNotFound(
                "Participant not found in the specified competition"
            )

        self.participants.delete_participant(participant_id, competition_id)
