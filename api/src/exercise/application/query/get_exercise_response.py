from ..exercise_dto import ExerciseDTO


class GetExerciseResponse:
    def __init__(
        self,
        exercise_id: str,
        competition_id: str,
        name: str,
        sets: int,
        reps: int,
        execution_order: int,
    ):
        self.__exercise_id: str = exercise_id
        self.__competition_id: str = competition_id
        self.__name: str = name
        self.__sets: int = sets
        self.__reps: int = reps
        self.__execution_order: int = execution_order

    @property
    def exercise_id(self):
        return self.__exercise_id

    @property
    def competition_id(self):
        return self.__competition_id

    @property
    def name(self):
        return self.__name

    @property
    def sets(self):
        return self.__sets

    @property
    def reps(self):
        return self.__reps

    @property
    def execution_order(self):
        return self.__execution_order

    @property
    def exercise_dto(self):
        return ExerciseDTO(
            exercise_id=self.exercise_id,
            competition_id=self.competition_id,
            name=self.name,
            sets=self.sets,
            reps=self.reps,
            execution_order=self.execution_order,
        )
