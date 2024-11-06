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
            "open": cls.OPEN,
            "started": cls.STARTED,
            "finished": cls.FINISHED,
            "cancelled": cls.CANCELLED,
        }
        status = status.lower()
        try:
            return status_map[status]
        except KeyError:
            raise InvalidCompetitionStatus("Invalid competition status")
