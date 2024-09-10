from ....shared.domain.competition_id import CompetitionId
from .execution_order import ExecutionOrder
from .exercise_id import ExerciseId
from .exercise_name import ExerciseName
from .exercise_reps import ExerciseReps
from .exercise_sets import ExerciseSets


class Exercise:
    class InvalidExercise(Exception):
        pass

    def __init__(
        self,
        exercise_id: ExerciseId,
        competition_id: CompetitionId,
        name: ExerciseName,
        sets: ExerciseSets,
        reps: ExerciseReps,
        execution_order: ExecutionOrder,
    ):
        self._exercise_id: ExerciseId = exercise_id
        self._competition_id: CompetitionId = competition_id
        self._name: ExerciseName = name
        self._sets: ExerciseSets = sets
        self._reps: ExerciseReps = reps
        self._execution_order: ExecutionOrder = execution_order

    @property
    def exercise_id(self):
        return self._exercise_id.value

    @property
    def competition_id(self):
        return self._competition_id.value

    @property
    def name(self):
        return self._name.value

    @property
    def sets(self):
        return self._sets.value

    @property
    def reps(self):
        return self._reps.value

    @property
    def execution_order(self):
        return self._execution_order.value

    @classmethod
    def add(
        cls,
        exercise_id: ExerciseId,
        competition_id: CompetitionId,
        name: ExerciseName,
        sets: ExerciseSets,
        reps: ExerciseReps,
        execution_order: ExecutionOrder,
    ):
        return cls(exercise_id, competition_id, name, sets, reps, execution_order)
