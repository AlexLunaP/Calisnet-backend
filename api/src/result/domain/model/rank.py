class Rank:

    class invalidRank(ValueError):
        pass

    def __init__(self, rank: int):
        self.__validate_rank(rank)
        self.__rank: int = rank

    @staticmethod
    def from_string(rank: str):
        return Rank(int(rank))

    @property
    def value(self):
        return self.__rank

    def __validate_rank(self, rank: int):
        if rank < 1:
            raise self.invalidRank("Rank number must be greater than 0")
