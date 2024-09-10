from ....shared.domain.competition_id import CompetitionId
from ....shared.domain.user_id import UserId
from ...domain.model.penalties import Penalties
from ...domain.model.rank import Rank
from ...domain.model.result import Result
from ...domain.model.result_id import ResultId
from ...domain.model.result_time import ResultTime
from ...domain.repository.results import Results


class CreateResult:
    def __init__(self, results: Results):
        self.results = results

    def handle(
        self,
        result_id: str,
        competition_id: str,
        participant_id: str,
        result_time: str,
        penalties: str,
        rank: str,
    ):

        result_id_object = ResultId.from_string(result_id)

        result = Result.add(
            result_id=result_id_object,
            competition_id=CompetitionId.from_string(competition_id),
            participant_id=UserId.from_string(participant_id),
            result_time=ResultTime.from_string(result_time),
            penalties=Penalties.from_string(penalties),
            rank=Rank.from_string(rank),
        )

        self.results.save(result)
