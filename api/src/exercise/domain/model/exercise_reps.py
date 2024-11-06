class ExerciseReps:

    class invalidExerciseReps(ValueError):
        pass

    def __init__(self, exercise_reps: int):
        self.__validate_exercise_reps(exercise_reps)
        self.__exercise_reps: int = exercise_reps

    @staticmethod
    def from_string(exercise_reps: str):
        return ExerciseReps(int(exercise_reps))

    @property
    def value(self):
        return self.__exercise_reps

    def __validate_exercise_reps(self, exercise_reps: int):
        if int(exercise_reps) < 1:
            raise self.invalidExerciseReps(
                "Exercise number of repetitions must be greater than 0"
            )
