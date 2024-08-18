from ....shared.domain.competition_id import CompetitionId


class Achievement:

    def __init__(self, competitionId: CompetitionId, rank: int):
        self.__competitionId: CompetitionId = competitionId
        self.__rank: int = rank

    @property
    def competitionId(self):
        return self.__competitionId.value

    @property
    def rank(self):
        return self.__rank
