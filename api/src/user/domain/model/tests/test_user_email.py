import faker
import pytest

from ..user_email import UserEmail

fake = faker.Faker()


class TestUserEmail:

    def test_constructor(self):
        expected_value = fake.email()

        user_email = UserEmail(expected_value)

        assert user_email.value == expected_value

    def test_from_string_constructor(self):
        expected_value = fake.email()

        user_email = UserEmail.from_string(expected_value)

        assert user_email.value == expected_value

    def test_empty_user_email(self):
        with pytest.raises(UserEmail.InvalidEmail):
            UserEmail("")

    def test_bad_user_email(self):
        with pytest.raises(UserEmail.InvalidEmail):
            UserEmail("John Doe@email.com")
