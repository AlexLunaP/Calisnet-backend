from uuid import UUID, uuid4

import pytest

from ..competition_id import CompetitionId


class TestCompetitionId:

    def test_constructor(self):
        random_id = uuid4()

        competition_id = CompetitionId(random_id)

        assert competition_id.value == random_id

    def test_from_string_constructor(self):
        random_id = str(uuid4())

        competition_id = CompetitionId.from_string(random_id)

        assert competition_id.value == UUID(random_id)

    def test_bad_competition_id(self):
        with pytest.raises(TypeError):
            CompetitionId("123")  # type: ignore
