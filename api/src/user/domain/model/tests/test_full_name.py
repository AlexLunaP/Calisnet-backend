import faker
import pytest

from ..full_name import FullName

fake = faker.Faker()


class TestFullName:

    def test_constructor(self):
        expected_value = fake.name()

        full_name = FullName(expected_value)

        assert full_name.value == expected_value

    def test_from_string_constructor(self):
        expected_value = fake.name()

        full_name = FullName.from_string(expected_value)

        assert full_name.value == expected_value

    def test_empty_full_name(self):
        with pytest.raises(FullName.InvalidFullName):
            FullName("")
