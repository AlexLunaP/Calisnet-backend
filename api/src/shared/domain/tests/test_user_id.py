from uuid import UUID, uuid4

import pytest

from ..user_id import UserId


class TestUserId:

    def test_constructor(self):
        randomId = uuid4()

        userId = UserId(randomId)

        assert userId.value == randomId

    def test_from_string_constructor(self):
        randomId = str(uuid4())

        userId = UserId.fromString(randomId)

        assert userId.value == UUID(randomId)

    def test_bad_user_id(self):
        with pytest.raises(TypeError):
            UserId("123")  # type: ignore
