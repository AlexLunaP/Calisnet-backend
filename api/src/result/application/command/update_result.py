from ...domain.exceptions.result_was_not_found import ResultWasNotFound
from ...domain.model.penalties import Penalties
from ...domain.model.rank import Rank
from ...domain.model.result_id import ResultId
from ...domain.model.result_time import ResultTime
from ...domain.repository.results import Results


class UpdateResult:
    def __init__(self, results: Results):
        self.results = results

    def handle(
        self,
        result_id: str,
        competition_id: str,
        participant_id: str,
        result_time: int,
        penalties: int,
        rank: int,
    ):

        result_id_object = ResultId.from_string(result_id)
        result = self.results.get_by_id(result_id_object)

        if not result:
            raise ResultWasNotFound("The result was not found")

        if result_time is not None:
            result.update_result_time(ResultTime.from_string(str(result_time)))
        if penalties is not None:
            result.update_penalties(Penalties.from_string(str(penalties)))
        if rank is not None:
            result.update_rank(Rank.from_string(str(rank)))

        self.results.update_result(result)
