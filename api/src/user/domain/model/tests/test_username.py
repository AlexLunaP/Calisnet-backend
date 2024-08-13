import faker
import pytest

from ..username import Username

fake = faker.Faker()


class TestUserName:

    def test_constructor(self):
        expectedValue = fake.first_name()

        userName = Username(expectedValue)

        assert userName.value == expectedValue

    def test_from_string_constructor(self):
        expectedValue = fake.first_name()

        userName = Username.fromString(expectedValue)

        assert userName.value == expectedValue

    def test_empty_username(self):
        with pytest.raises(Username.InvalidUserName):
            Username("")

    def test_username_with_spaces(self):
        with pytest.raises(Username.InvalidUserName):
            Username("Mark Knopfler")
