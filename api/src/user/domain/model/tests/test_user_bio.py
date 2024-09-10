import faker
import pytest

from ..user_bio import UserBio

fake = faker.Faker()


class TestUserBio:

    def test_constructor(self):
        expected_value = fake.text(max_nb_chars=UserBio.MAX_BIO_LENGTH)

        user_bio = UserBio(expected_value)

        assert user_bio.value == expected_value

    def test_from_string_constructor(self):
        expected_value = fake.text(max_nb_chars=UserBio.MAX_BIO_LENGTH)

        user_bio = UserBio.from_string(expected_value)

        assert user_bio.value == expected_value

    def test_empty_user_bio(self):
        with pytest.raises(UserBio.InvalidUserBio):
            UserBio("")

    def test_create_user_bio_exceed_max_length(self):
        with pytest.raises(UserBio.InvalidUserBio):
            UserBio(fake.text(max_nb_chars=UserBio.MAX_BIO_LENGTH + 255))
