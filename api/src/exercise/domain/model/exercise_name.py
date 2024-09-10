class ExerciseName:
    class InvalidExerciseName(Exception):
        pass

    def __init__(self, exercise_name: str):
        self.__validate_exercise_name_not_empty(exercise_name)
        self.__exercise_name: str = exercise_name

    @staticmethod
    def from_string(exercise_name: str):
        return ExerciseName(exercise_name)

    @property
    def value(self):
        return self.__exercise_name

    def __validate_exercise_name_not_empty(self, exercise_name: str):
        if len(exercise_name) == 0:
            raise self.InvalidExerciseName("Exercise name cannot be empty")
