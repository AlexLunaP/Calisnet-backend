from typing import TypedDict


class ResultDTO(TypedDict):
    result_id: str
    competition_id: str
    participant_id: str
    result_time: str
    penalties: str
    rank: str
