from ...domain.model.exercise_id import ExerciseId
from ...domain.repository.exercises import Exercises


class DeleteExercise:
    def __init__(self, exercises: Exercises):
        self.exercises = exercises

    def handle(
        self,
        exercise_id: str,
    ):
        exercise_id_object = ExerciseId.from_string(exercise_id)
        exercise = self.exercises.get_by_id(exercise_id_object)
        if not exercise:
            raise ValueError("Exercise not found")

        self.exercises.delete_exercise(exercise_id_object)
