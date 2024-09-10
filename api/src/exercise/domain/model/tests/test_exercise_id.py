from uuid import UUID, uuid4

import pytest

from ..exercise_id import ExerciseId


class TestExerciseId:

    def test_constructor(self):
        random_id = uuid4()

        exercise_id = ExerciseId(random_id)

        assert exercise_id.value == random_id

    def test_from_string_constructor(self):
        random_id = str(uuid4())

        exercise_id = ExerciseId.from_string(random_id)

        assert exercise_id.value == UUID(random_id)

    def test_bad_exercise_id(self):
        with pytest.raises(TypeError):
            ExerciseId("123")  # type: ignore
