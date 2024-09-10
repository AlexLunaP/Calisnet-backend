from uuid import UUID


class ExerciseId:

    def __init__(self, exercise_id: UUID):
        self.validate_exercise_id(exercise_id)
        self.__value: UUID = exercise_id

    @staticmethod
    def from_string(exercise_id: str):
        return ExerciseId(UUID(exercise_id))

    @property
    def value(self):
        return self.__value

    def validate_exercise_id(self, exercise_id: UUID):
        if not isinstance(exercise_id, UUID):
            raise TypeError("Exercise ID must be an UUID instance")
