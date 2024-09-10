class CompetitionDescription:

    MAX_DESCRIPTION_LENGTH = 250

    class InvalidCompetitionDescription(Exception):
        pass

    def __init__(self, competition_description: str):
        self.__validate_competition_description_not_empty(competition_description)
        self.__validate_competition_description_length(competition_description)
        self.__competition_description: str = competition_description

    @staticmethod
    def from_string(competition_description: str):
        return CompetitionDescription(competition_description)

    @property
    def value(self):
        return self.__competition_description

    def __validate_competition_description_not_empty(
        self, competition_description: str
    ):
        if len(competition_description) == 0:
            raise self.InvalidCompetitionDescription(
                "Competition description cannot be empty"
            )

    def __validate_competition_description_length(self, competition_description: str):
        if len(competition_description) > self.MAX_DESCRIPTION_LENGTH:
            raise self.InvalidCompetitionDescription(
                "Competition description cannot exceed "
                + f"{self.MAX_DESCRIPTION_LENGTH} characters"
            )
