from typing import List, Optional

from ..exercise_dto import ExerciseDTO


class GetExercisesByCompetitionIdResponse:

    def __init__(self, exercises: Optional[List[ExerciseDTO]] = None):
        self.__exercises = exercises if exercises is not None else []

    @property
    def exercises(self) -> List[ExerciseDTO]:
        return self.__exercises

    def add_exercise(self, exercise: ExerciseDTO) -> List[ExerciseDTO] | None:
        self.__exercises.append(exercise)
