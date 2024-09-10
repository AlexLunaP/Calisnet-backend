from uuid import uuid4

import faker
import pytest

from .....shared.domain.competition_id import CompetitionId
from .....shared.domain.user_id import UserId
from ....application.command.create_competition import CreateCompetition
from ....domain.exceptions.competition_id_already_exists import (
    CompetitionIdAlreadyExists,
)
from ....domain.model.competition import Competition
from ....domain.model.competition_status import CompetitionStatus
from ....domain.repository.competitions import Competitions

fake = faker.Faker()


@pytest.fixture
def mocked_competitions(mocker):
    return mocker.Mock(spec=Competitions)


@pytest.fixture
def create_competition_instance(mocked_competitions):
    return CreateCompetition(competitions=mocked_competitions)


class TestCreateCompetition:

    def test_create_new_competition(
        self, create_competition_instance, mocked_competitions
    ):

        # Mock behavior of Competitions repository
        mocked_competitions.get_by_id.return_value = None

        mocked_details = {
            "name": fake.name(),
            "description": fake.text(),
            "date": fake.future_datetime().strftime("%Y-%m-%d"),
            "location": fake.address(),
            "image": fake.url(),
            "participant_limit": 10,
            "penalty_time": 10,
            "status": CompetitionStatus.OPEN.value,
        }

        create_competition_instance.handle(
            competition_id=str(uuid4()),
            organizer_id=str(uuid4()),
            name=mocked_details["name"],
            description=mocked_details["description"],
            date=mocked_details["date"],
            location=mocked_details["location"],
            image=mocked_details["image"],
            participant_limit=mocked_details["participant_limit"],
            penalty_time=mocked_details["penalty_time"],
            status=mocked_details["status"],
        )
        mocked_competitions.save.assert_called_once()

    def test_do_not_create_competition_if_competition_id_already_exists(
        self, create_competition_instance, mocked_competitions
    ):

        mocked_details = {
            "name": fake.name(),
            "description": fake.text(),
            "date": fake.future_datetime().strftime("%Y-%m-%d"),
            "location": fake.address(),
            "image": fake.url(),
            "participant_limit": 10,
            "penalty_time": 10,
            "status": CompetitionStatus.OPEN.value,
        }

        # Mock behavior of Competitions repository
        # to return a competition with the same ID
        mocked_competitions.get_by_id.return_value = Competition(
            competition_id=CompetitionId.from_string(str(uuid4())),
            organizer_id=UserId.from_string(str(uuid4())),
            name=mocked_details["name"],
            description=mocked_details["description"],
            date=mocked_details["date"],
            location=mocked_details["location"],
            image=mocked_details["image"],
            participant_limit=mocked_details["participant_limit"],
            penalty_time=mocked_details["penalty_time"],
            status=CompetitionStatus.OPEN,
        )

        with pytest.raises(CompetitionIdAlreadyExists):
            create_competition_instance.handle(
                competition_id=str(uuid4()),
                organizer_id=str(uuid4()),
                name=mocked_details["name"],
                description=mocked_details["description"],
                date=mocked_details["date"],
                location=mocked_details["location"],
                image=mocked_details["image"],
                participant_limit=mocked_details["participant_limit"],
                penalty_time=mocked_details["penalty_time"],
                status=mocked_details["status"],
            )
