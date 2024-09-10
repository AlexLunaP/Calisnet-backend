from ..result_dto import ResultDTO


class GetResultResponse:
    def __init__(
        self,
        result_id: str,
        participant_id: str,
        competition_id: str,
        result_time: int,
        penalties: int,
        rank: int,
    ):
        self.__result_id: str = result_id
        self.__participant_id: str = participant_id
        self.__competition_id: str = competition_id
        self.__result_time: int = result_time
        self.__penalties: int = penalties
        self.__rank: int = rank

    @property
    def result_id(self):
        return self.__result_id

    @property
    def participant_id(self):
        return self.__participant_id

    @property
    def competition_id(self):
        return self.__competition_id

    @property
    def result_time(self):
        return self.__result_time

    @property
    def penalties(self):
        return self.__penalties

    @property
    def rank(self):
        return self.__rank

    @property
    def result_dto(self):
        return ResultDTO(
            result_id=self.result_id,
            participant_id=self.participant_id,
            competition_id=self.competition_id,
            result_time=str(self.result_time),
            penalties=str(self.penalties),
            rank=str(self.rank),
        )
