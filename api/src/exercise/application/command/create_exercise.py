from ....shared.domain.competition_id import CompetitionId
from ...domain.exceptions.exercise_id_already_exists import ExerciseIdAlreadyExists
from ...domain.model.execution_order import ExecutionOrder
from ...domain.model.exercise import Exercise
from ...domain.model.exercise_id import ExerciseId
from ...domain.model.exercise_name import ExerciseName
from ...domain.model.exercise_reps import ExerciseReps
from ...domain.model.exercise_sets import ExerciseSets
from ...domain.repository.exercises import Exercises


class CreateExercise:
    def __init__(self, exercises: Exercises):
        self.exercises = exercises

    def handle(
        self,
        exercise_id: str,
        competition_id: str,
        name: str,
        sets: int,
        reps: int,
        execution_order: int,
    ):

        exercise_id_object = ExerciseId.from_string(exercise_id)

        if self.exercises.get_by_id(exercise_id_object):
            raise ExerciseIdAlreadyExists("The exercise ID already exists")

        exercise = Exercise.add(
            exercise_id=exercise_id_object,
            competition_id=CompetitionId.from_string(competition_id),
            name=ExerciseName.from_string(name),
            sets=ExerciseSets(sets),
            reps=ExerciseReps(reps),
            execution_order=ExecutionOrder(execution_order),
        )

        self.exercises.save(exercise)
