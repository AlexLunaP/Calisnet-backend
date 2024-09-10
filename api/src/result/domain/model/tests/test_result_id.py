from uuid import UUID, uuid4

import pytest

from ..result_id import ResultId


class TesResultId:

    def test_constructor(self):
        random_id = uuid4()

        result_id = ResultId(random_id)

        assert result_id.value == result_id

    def test_from_string_constructor(self):
        random_id = str(uuid4())

        result_id = ResultId.from_string(random_id)

        assert result_id.value == UUID(random_id)

    def test_bad_result_id(self):
        with pytest.raises(TypeError):
            ResultId("123")  # type: ignore
