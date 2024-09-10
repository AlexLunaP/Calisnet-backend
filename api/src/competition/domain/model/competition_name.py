class CompetitionName:
    class InvalidCompetitionName(Exception):
        pass

    def __init__(self, competition_name: str):
        self._validate_competition_name_not_empty(competition_name)
        self.__value: str = competition_name

    @staticmethod
    def from_string(competition_name: str):
        return CompetitionName(competition_name)

    @property
    def value(self):
        return self.__value

    def _validate_competition_name_not_empty(self, competition_name: str):
        if len(competition_name) == 0:
            raise self.InvalidCompetitionName("Username cannot be empty")
