from uuid import uuid4

import faker
import pytest

from ....domain.repository.results import Results
from ...command.create_result import CreateResult

fake = faker.Faker()


@pytest.fixture
def mocked_results(mocker):
    return mocker.Mock(spec=Results)


@pytest.fixture
def create_result_instance(mocked_results):
    return CreateResult(results=mocked_results)


class TestCreateResult:

    def test_create_new_result(self, create_result_instance, mocked_results):

        # Mock behavior of Results repository
        mocked_results.get_by_id.return_value = None

        mocked_details = {
            "competition_id": str(uuid4()),
            "participant_id": str(uuid4()),
            "result_time": fake.time(),
            "penalties": fake.random_int(),
            "rank": fake.random_int(),
        }

        create_result_instance.handle(
            result_id=str(uuid4()),
            competition_id=mocked_details["competition_id"],
            participant_id=mocked_details["participant_id"],
            result_time=mocked_details["result_time"],
            penalties=mocked_details["penalties"],
            rank=mocked_details["rank"],
        )
        mocked_results.save.assert_called_once()
