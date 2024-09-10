class ParticipantName:
    class InvalidParticipantName(Exception):
        pass

    def __init__(self, participant_name: str):
        self.__validate_participant_name_not_empty(participant_name)
        self.__participant_name: str = participant_name

    @staticmethod
    def from_string(participant_name: str):
        return ParticipantName(participant_name)

    @property
    def value(self):
        return self.__participant_name

    def __validate_participant_name_not_empty(self, participant_name: str):
        if len(participant_name) == 0:
            raise self.InvalidParticipantName("Participant name cannot be empty")
