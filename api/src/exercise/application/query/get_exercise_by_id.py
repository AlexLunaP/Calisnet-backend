from ...domain.model.exercise_id import ExerciseId
from ...domain.repository.exercises import Exercises
from .get_exercise_response import GetExerciseResponse


class GetExerciseByIdQuery:
    def __init__(self, exercise_id: str):
        self.__exercise_id: str = exercise_id

    @property
    def exercise_id(self):
        return self.__exercise_id


class GetExerciseByIdHandler:
    def __init__(self, exercises: Exercises):
        self.__exercises: Exercises = exercises

    def handle(self, query: GetExerciseByIdQuery):
        exercise_id = ExerciseId.from_string(query.exercise_id)

        exercise = self.__exercises.get_by_id(exercise_id)

        if not exercise:
            return None

        return GetExerciseResponse(
            exercise_id=str(exercise.exercise_id),
            competition_id=str(exercise.competition_id),
            name=exercise.name,
            sets=exercise.sets,
            reps=exercise.reps,
            execution_order=exercise.execution_order,
        )
