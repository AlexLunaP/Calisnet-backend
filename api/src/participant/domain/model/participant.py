from ....shared.domain.competition_id import CompetitionId
from .participant_id import ParticipantId
from .participant_name import ParticipantName


class Participant:

    class InvalidParticipant(Exception):
        pass

    def __init__(
        self,
        participant_id: ParticipantId,
        competition_id: CompetitionId,
        name: ParticipantName,
    ):
        self._participant_id: ParticipantId = participant_id
        self._competition_id: CompetitionId = competition_id
        self._name: ParticipantName = name

    @property
    def participant_id(self):
        return self._participant_id.value

    @property
    def competition_id(self):
        return self._competition_id.value

    @property
    def name(self):
        return self._name.value

    @classmethod
    def add(
        cls,
        participant_id: ParticipantId,
        competition_id: CompetitionId,
        name: ParticipantName,
    ):
        return cls(participant_id, competition_id, name)
