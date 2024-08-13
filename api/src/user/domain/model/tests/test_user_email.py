import faker
import pytest

from ..user_email import UserEmail

fake = faker.Faker()


class TestUserEmail:

    def test_constructor(self):
        expectedValue = fake.email()

        userEmail = UserEmail(expectedValue)

        assert userEmail.value == expectedValue

    def test_from_string_constructor(self):
        expectedValue = fake.email()

        userEmail = UserEmail.fromString(expectedValue)

        assert userEmail.value == expectedValue

    def test_empty_userEmail(self):
        with pytest.raises(UserEmail.InvalidEmail):
            UserEmail("")

    def test_bad_userEmail(self):
        with pytest.raises(UserEmail.InvalidEmail):
            UserEmail("John Doe@email.com")
