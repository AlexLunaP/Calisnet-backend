from uuid import UUID


class ParticipantId:

    def __init__(self, participant_id: UUID):
        self.validate_participant_id(participant_id)
        self.__value: UUID = participant_id

    @staticmethod
    def from_string(participant_id: str):
        return ParticipantId(UUID(participant_id))

    @property
    def value(self):
        return self.__value

    def validate_participant_id(self, participant_id: UUID):
        if not isinstance(participant_id, UUID):
            raise TypeError("Participant ID must be an UUID instance")
