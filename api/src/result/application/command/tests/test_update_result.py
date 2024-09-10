from uuid import uuid4

import faker
import pytest
from pytest_mock import MockerFixture

from .....shared.domain.competition_id import CompetitionId
from .....shared.domain.user_id import UserId
from ....application.command.update_result import UpdateResult
from ....domain.exceptions.result_was_not_found import ResultWasNotFound
from ....domain.model.penalties import Penalties
from ....domain.model.rank import Rank
from ....domain.model.result import Result, ResultId
from ....domain.model.result_time import ResultTime
from ....domain.repository.results import Results

fake = faker.Faker()


@pytest.fixture
def mocked_results(mocker: MockerFixture):
    return mocker.Mock(spec=Results)


@pytest.fixture
def create_result_instance(mocked_results):
    return UpdateResult(results=mocked_results)


class TestUpdateResult:

    def test_update_result(self, create_result_instance, mocked_results):
        result_id_mock = uuid4()
        competition_id_mock = uuid4()
        participant_id_mock = uuid4()

        # Mock behavior of Results repository
        mocked_results.get_by_id.return_value = Result(
            result_id=ResultId(result_id_mock),
            competition_id=CompetitionId(competition_id_mock),
            participant_id=UserId(participant_id_mock),
            result_time=ResultTime(fake.time()),
            penalties=Penalties(fake.random_int()),
            rank=Rank(fake.random_int()),
        )

        create_result_instance.handle(
            result_id=str(result_id_mock),
            competition_id=str(competition_id_mock),
            participant_id=str(participant_id_mock),
            result_time=fake.time(),
            penalties=fake.random_int(),
            rank=fake.random_int(),
        )

        mocked_results.update_result.assert_called_once()

    def test_do_not_update_result_if_result_was_not_found(
        self, create_result_instance, mocked_results
    ):
        result_id_mock = uuid4()

        # Mock behavior of Results repository
        mocked_results.get_by_id.return_value = None

        with pytest.raises(ResultWasNotFound):
            create_result_instance.handle(
                result_id=str(result_id_mock),
                competition_id=str(uuid4()),
                participant_id=str(uuid4()),
                result_time=fake.time(),
                penalties=fake.random_int(),
                rank=fake.random_int(),
            )
