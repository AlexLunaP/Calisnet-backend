from uuid import UUID, uuid4

import pytest

from ..user_id import UserId


class TestUserId:

    def test_constructor(self):
        random_id = uuid4()

        user_id = UserId(random_id)

        assert user_id.value == random_id

    def test_from_string_constructor(self):
        random_id = str(uuid4())

        user_id = UserId.from_string(random_id)

        assert user_id.value == UUID(random_id)

    def test_bad_user_id(self):
        with pytest.raises(TypeError):
            UserId("123")  # type: ignore
