from uuid import UUID


class CompetitionId:

    def __init__(self, competition_id: UUID):
        self.validate_competition_id(competition_id)
        self.__value: UUID = competition_id

    @staticmethod
    def from_string(competition_id: str):
        return CompetitionId(UUID(competition_id))

    @property
    def value(self):
        return self.__value

    def validate_competition_id(self, competition_id: UUID):
        if not isinstance(competition_id, UUID):
            raise TypeError("Competition ID must be an UUID instance")
