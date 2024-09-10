from ....shared.domain.competition_id import CompetitionId
from ...domain.model.participant import Participant
from ...domain.model.participant_id import ParticipantId
from ...domain.model.participant_name import ParticipantName
from ...domain.repository.participants import Participants


class CreateParticipant:
    def __init__(self, participants: Participants):
        self.participants = participants

    def handle(
        self,
        participant_id: str,
        competition_id: str,
        name: str,
    ):

        participant_id_object = ParticipantId.from_string(participant_id)

        participant = Participant.add(
            participant_id=participant_id_object,
            competition_id=CompetitionId.from_string(competition_id),
            name=ParticipantName.from_string(name),
        )

        self.participants.save(participant)
