from ....shared.domain.competition_id import CompetitionId
from ....shared.domain.user_id import UserId
from .penalties import Penalties
from .rank import Rank
from .result_id import ResultId
from .result_time import ResultTime


class Result:
    def __init__(
        self,
        result_id: ResultId,
        competition_id: CompetitionId,
        participant_id: UserId,
        result_time: ResultTime,
        penalties: Penalties,
        rank: Rank,
    ):
        self._result_id: ResultId = result_id
        self._competition_id: CompetitionId = competition_id
        self._participant_id: UserId = participant_id
        self._result_time: ResultTime = result_time
        self._penalties: Penalties = penalties
        self._rank: Rank = rank if rank else Rank(1)

    @property
    def result_id(self):
        return self._result_id.value

    @property
    def competition_id(self):
        return self._competition_id.value

    @property
    def participant_id(self):
        return self._participant_id.value

    @property
    def result_time(self):
        return self._result_time.value

    @property
    def penalties(self):
        return self._penalties.value

    @property
    def rank(self):
        return self._rank.value

    @classmethod
    def add(
        cls,
        result_id: ResultId,
        competition_id: CompetitionId,
        participant_id: UserId,
        result_time: ResultTime,
        penalties: Penalties,
        rank: Rank,
    ):
        return cls(
            result_id, competition_id, participant_id, result_time, penalties, rank
        )

    def update_result_time(self, result_time: ResultTime):
        self._result_time = result_time

    def update_penalties(self, penalties: Penalties):
        self._penalties = penalties

    def update_rank(self, rank: Rank):
        self._rank = rank
