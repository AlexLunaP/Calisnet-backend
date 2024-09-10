class ParticipantLimit:
    class invalidParticipantLimit(ValueError):
        pass

    def __init__(self, participant_limit: int):
        self.__validate_participant_limit(participant_limit)
        self.__participant_limit: int = participant_limit

    @staticmethod
    def from_string(participant_limit: str):
        return ParticipantLimit(int(participant_limit))

    @property
    def value(self):
        return self.__participant_limit

    def __validate_participant_limit(self, participant_limit: int):
        if participant_limit < 0:
            raise self.invalidParticipantLimit("Participant limit cannot be negative")
