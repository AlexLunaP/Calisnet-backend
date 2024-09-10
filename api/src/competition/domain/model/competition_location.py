class CompetitionLocation:

    class InvalidCompetitionLocation(Exception):
        pass

    def __init__(self, competition_location: str):
        self.__validate_competition_location_not_empty(competition_location)
        self.__competition_location: str = competition_location

    @staticmethod
    def from_string(competition_location: str):
        return CompetitionLocation(competition_location)

    @property
    def value(self):
        return self.__competition_location

    def __validate_competition_location_not_empty(self, competition_location: str):
        if len(competition_location) == 0:
            raise self.InvalidCompetitionLocation(
                "Competition location cannot be empty"
            )
