from enum import Enum

from ..exceptions.invalid_competition_status import InvalidCompetitionStatus


class CompetitionStatus(Enum):
    OPEN = "Open"
    STARTED = "Started"
    FINISHED = "Finished"
    CANCELLED = "Cancelled"

    def __str__(self):
        return self.value

    @classmethod
    def from_string(cls, status: str) -> "CompetitionStatus":
        status_map = {
            "Open": cls.OPEN,
            "Started": cls.STARTED,
            "Finished": cls.FINISHED,
            "Cancelled": cls.CANCELLED,
        }
        try:
            return status_map[status]
        except KeyError:
            raise InvalidCompetitionStatus("Invalid competition status")
