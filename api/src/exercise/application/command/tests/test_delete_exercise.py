from uuid import uuid4

import faker
import pytest

from ....domain.repository.exercises import Exercises
from ...command.delete_exercise import DeleteExercise

fake = faker.Faker()


@pytest.fixture
def mocked_exercises(mocker):
    return mocker.Mock(spec=Exercises)


@pytest.fixture
def delete_exercise_instance(mocked_exercises):
    return DeleteExercise(exercises=mocked_exercises)


class TestDeleteExercise:

    def test_delete_exercise(self, delete_exercise_instance, mocked_exercises):
        exercise_id = str(uuid4())
        mocked_exercises.get_by_id.return_value = {
            "exercise_id": exercise_id,
            "competition_id": uuid4(),
            "name": "Test Exercise",
            "sets": 3,
            "reps": 10,
            "execution_order": 1,
        }

        delete_exercise_instance.handle(exercise_id)
        mocked_exercises.get_by_id.assert_called_once()
        mocked_exercises.delete_exercise.assert_called_once()

    def test_do_not_delete_nonexistent_exercise(
        self, delete_exercise_instance, mocked_exercises
    ):
        # Mock behavior of Exercises repository to return None
        exercise_id = str(uuid4())
        mocked_exercises.get_by_id.return_value = None

        with pytest.raises(ValueError):
            delete_exercise_instance.handle(exercise_id)
        mocked_exercises.get_by_id.assert_called_once()
        mocked_exercises.delete_exercise.assert_not_called()
