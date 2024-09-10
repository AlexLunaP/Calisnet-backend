from typing import TypedDict


class ParticipantDTO(TypedDict):
    participant_id: str
    competition_id: str
    name: str
