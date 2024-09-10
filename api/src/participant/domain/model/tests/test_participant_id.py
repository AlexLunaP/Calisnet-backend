from uuid import UUID, uuid4

import pytest

from ..participant_id import ParticipantId


class TestParticipantId:

    def test_constructor(self):
        random_id = uuid4()

        participant_id = ParticipantId(random_id)

        assert participant_id.value == random_id

    def test_from_string_constructor(self):
        random_id = str(uuid4())

        participant_id = ParticipantId.from_string(random_id)

        assert participant_id.value == UUID(random_id)

    def test_bad_exercise_id(self):
        with pytest.raises(TypeError):
            ParticipantId("123")  # type: ignore
