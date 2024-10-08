from dependency_injector.wiring import Provide, inject

from ...application.command.create_exercise import CreateExercise
from ...application.exercise_dto import ExerciseDTO
from ...application.query.get_exercise_by_id import (
    GetExerciseByIdHandler,
    GetExerciseByIdQuery,
)
from ...application.query.get_exercises_by_competition_id import (
    GetExercisesByCompetitionIdHandler,
    GetExercisesByCompetitionIdQuery,
)
from ...domain.repository.exercises import Exercises


class ExerciseService:

    @inject
    def __init__(self, exercises: Exercises = Provide["EXERCISES"]):
        self.exercises: Exercises = exercises
        self.create_exercise_command = CreateExercise(exercises)
        self.get_exercise_by_id_handler = GetExerciseByIdHandler(exercises)
        self.get_exercises_by_competition_id_handler = (
            GetExercisesByCompetitionIdHandler(exercises)
        )

    def create_exercise(self, exercise_dto: ExerciseDTO):
        exercise_id = exercise_dto["exercise_id"]
        competition_id = exercise_dto["competition_id"]
        name = exercise_dto["name"]
        sets = exercise_dto["sets"]
        reps = exercise_dto["reps"]
        execution_order = exercise_dto["execution_order"]

        self.create_exercise_command.handle(
            exercise_id,
            competition_id,
            name,
            sets,
            reps,
            execution_order,
        )

    def get_exercise(self, exercise_id: str):
        exercise = self.get_exercise_by_id_handler.handle(
            GetExerciseByIdQuery(exercise_id)
        )

        if not exercise:
            return None

        return exercise.exercise_dto

    def get_exercises_by_competition(self, competition_id: str):
        exercises = self.get_exercises_by_competition_id_handler.handle(
            GetExercisesByCompetitionIdQuery(competition_id)
        )

        if not exercises:
            return None

        return exercises.exercises
