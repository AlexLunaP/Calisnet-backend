from uuid import uuid4

import faker
import pytest

from ....domain.exceptions.participant_was_not_found import ParticipantWasNotFound
from ....domain.repository.participants import Participants
from ...command.delete_participant import DeleteParticipant

fake = faker.Faker()


@pytest.fixture
def mocked_participants(mocker):
    return mocker.Mock(spec=Participants)


@pytest.fixture
def delete_participant_instance(mocked_participants):
    return DeleteParticipant(participants=mocked_participants)


class TestDeleteParticipant:

    def test_delete_participant(self, delete_participant_instance, mocked_participants):
        participant_id = str(uuid4())
        competition_id = str(uuid4())
        mocked_participants.get_by_participant_id.return_value = [
            {
                "participant_id": participant_id,
                "competition_id": competition_id,
                "name": "Test Participant",
            }
        ]

        delete_participant_instance.handle(participant_id, competition_id)
        mocked_participants.delete_participant.assert_called_with(
            participant_id, competition_id
        )

    def test_do_not_delete_nonexistent_participant(
        self, delete_participant_instance, mocked_participants
    ):
        participant_id = str(uuid4())
        competition_id = str(uuid4())
        mocked_participants.get_by_participant_id.return_value = None

        with pytest.raises(ParticipantWasNotFound):
            delete_participant_instance.handle(participant_id, competition_id)
        mocked_participants.delete_participant.assert_not_called()
