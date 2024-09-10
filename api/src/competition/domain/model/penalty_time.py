class PenaltyTime:

    class invalidPenaltyTime(Exception):
        pass

    def __init__(self, penalty_time: int):
        self.__validate_penalty_time(penalty_time)
        self.__penalty_time: int = penalty_time

    @staticmethod
    def from_string(penalty_time: str):
        return PenaltyTime(int(penalty_time))

    @property
    def value(self):
        return self.__penalty_time

    def __validate_penalty_time(self, penalty_time: int):
        if penalty_time < 0:
            raise self.invalidPenaltyTime("Penalty time cannot be negative")
