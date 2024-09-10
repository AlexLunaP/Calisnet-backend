import faker
import pytest

from ..username import Username

fake = faker.Faker()


class TestUsername:

    def test_constructor(self):
        expected_value = fake.first_name()

        username = Username(expected_value)

        assert username.value == expected_value

    def test_from_string_constructor(self):
        expected_value = fake.first_name()

        username = Username.from_string(expected_value)

        assert username.value == expected_value

    def test_empty_username(self):
        with pytest.raises(Username.InvalidUsername):
            Username("")

    def test_username_with_spaces(self):
        with pytest.raises(Username.InvalidUsername):
            Username("Mark Knopfler")
