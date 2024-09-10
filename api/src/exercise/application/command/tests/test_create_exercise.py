from uuid import uuid4

import faker
import pytest

from ....domain.repository.exercises import Exercises
from ...command.create_exercise import CreateExercise

fake = faker.Faker()


@pytest.fixture
def mocked_exercises(mocker):
    return mocker.Mock(spec=Exercises)


@pytest.fixture
def create_exercise_instance(mocked_exercises):
    return CreateExercise(exercises=mocked_exercises)


class TestCreateExercise:

    def test_create_new_exercise(self, create_exercise_instance, mocked_exercises):

        # Mock behavior of Exercises repository
        mocked_exercises.get_by_id.return_value = None

        mocked_details = {
            "competition_id": str(uuid4()),
            "name": fake.name(),
            "sets": 10,
            "reps": 10,
            "execution_order": 1,
        }

        create_exercise_instance.handle(
            exercise_id=str(uuid4()),
            competition_id=mocked_details["competition_id"],
            name=mocked_details["name"],
            sets=mocked_details["sets"],
            reps=mocked_details["reps"],
            execution_order=mocked_details["execution_order"],
        )
        mocked_exercises.save.assert_called_once()
