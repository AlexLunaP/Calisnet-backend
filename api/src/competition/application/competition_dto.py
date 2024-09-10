from typing import Optional, TypedDict


class CompetitionDTO(TypedDict):
    competition_id: str
    organizer_id: str
    name: str
    description: str
    date: str
    location: str
    image: str
    participant_limit: Optional[int]
    penalty_time: int
    status: str
