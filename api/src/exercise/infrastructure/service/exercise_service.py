from typing import Optional
from uuid import uuid4

from dependency_injector.wiring import Provide, inject
from flask_jwt_extended import get_current_user
from werkzeug.exceptions import NotFound, Unauthorized

from ....competition.infrastructure.service.competition_service import (
    CompetitionService,
)
from ...application.command.create_exercise import CreateExercise
from ...application.command.delete_exercise import DeleteExercise
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
        self.delete_exercise_command = DeleteExercise(exercises)

    def create_exercise(self, exercise_dto: ExerciseDTO):
        exercise_id = str(uuid4())
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

    def get_exercises(
        self,
        competition_id: Optional[str] = None,
    ):
        exercises = None

        if competition_id:
            exercises = self.get_exercises_by_competition_id_handler.handle(
                GetExercisesByCompetitionIdQuery(competition_id)
            )

        if not exercises:
            return None

        return exercises.exercises

    def delete_exercise(self, exercise_id: str):
        exercise = self.get_exercise(exercise_id)
        if not exercise:
            raise NotFound("Exercise was not found")

        competition_service: CompetitionService = CompetitionService()
        competition = competition_service.get_competition(exercise["competition_id"])
        if not competition:
            raise NotFound("Competition was not found")

        current_user_id: str = get_current_user()
        if current_user_id != competition["organizer_id"]:
            raise Unauthorized("Not allowed to modify the competition of another user.")

        self.delete_exercise_command.handle(exercise_id)
