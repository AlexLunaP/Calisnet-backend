from typing import TypedDict


class ExerciseDTO(TypedDict):
    exercise_id: str
    competition_id: str
    name: str
    sets: int
    reps: int
    execution_order: int
