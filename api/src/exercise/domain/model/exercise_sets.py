class ExerciseSets:

    class invalidExerciseSets(ValueError):
        pass

    def __init__(self, exercise_sets: int):
        self.__validate_exercise_sets(exercise_sets)
        self.__exercise_sets: int = exercise_sets

    @staticmethod
    def from_string(exercise_sets: str):
        return ExerciseSets(int(exercise_sets))

    @property
    def value(self):
        return self.__exercise_sets

    def __validate_exercise_sets(self, exercise_sets: int):
        if int(exercise_sets) < 1:
            raise self.invalidExerciseSets(
                "Exercise number of sets must be greater than 0"
            )
