from datetime import datetime

from ....shared.domain.competition_id import CompetitionId


class CompetitionHistoryEntry:

    def __init__(
        self,
        competition_id,
        date,
        time,
        rank,
    ):
        self._competition_id: CompetitionId = competition_id
        self._date: datetime = date
        self._finalTime: int = time
        self._rank: int = rank

    @property
    def competitionId(self):
        return self._competition_id.value

    @property
    def date(self):
        return self._date

    @property
    def time(self):
        return self._finalTime

    @property
    def rank(self):
        return self._rank
