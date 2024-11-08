from uuid import uuid4

import faker
import pytest

from ....domain.repository.participants import Participants
from ...command.create_participant import CreateParticipant

fake = faker.Faker()


@pytest.fixture
def mocked_participants(mocker):
    return mocker.Mock(spec=Participants)


@pytest.fixture
def create_participant_instance(mocked_participants):
    return CreateParticipant(participants=mocked_participants)


class TestCreateParticipant:

    def test_create_new_participant(
        self, create_participant_instance, mocked_participants
    ):

        mocked_details = {
            "participant_id": str(uuid4()),
            "competition_id": str(uuid4()),
            "name": fake.name(),
        }

        create_participant_instance.handle(
            participant_id=str(uuid4()),
            competition_id=mocked_details["competition_id"],
            name=mocked_details["name"],
        )
        mocked_participants.save.assert_called_once()
