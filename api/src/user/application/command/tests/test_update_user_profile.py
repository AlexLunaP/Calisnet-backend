from datetime import datetime
from uuid import UUID, uuid4

import faker
import pytest
from pytest_mock import mocker

from .....shared.domain.user_id import UserId
from ....domain.exception.user_was_not_found import UserWasNotFound
from ....domain.model.user_email import UserEmail
from ....domain.model.user_password import UserPassword
from ....domain.model.username import Username
from ....domain.repository.users import User, Users
from ..update_user_profile import UpdateUserProfile

fake = faker.Faker()


@pytest.fixture
def mocked_users(mocker):
    return mocker.Mock(spec=Users)


@pytest.fixture
def update_user_profile_instance(mocked_users):
    return UpdateUserProfile(users=mocked_users)


class TestUpdateUserProfile:

    def test_update_user_profile(self, update_user_profile_instance, mocked_users):
        userIdMock = uuid4()

        # Mock behavior of Users repository
        mocked_users.getById.return_value = User(
            userId=UserId(userIdMock),
            username=Username(fake.first_name()),
            userEmail=UserEmail(fake.email()),
            userPassword=UserPassword(fake.password()),
        )

        update_user_profile_instance.handle(
            userId=str(userIdMock),
            bio=fake.text(),
            birthdate=fake.date_of_birth().strftime("%d/%m/%Y"),
            profilePicUrl=fake.image_url(),
            socialLinks={"github": fake.url()},
        )

        mocked_users.updateUserProfile.assert_called_once()

    def test_do_not_update_user_profile_if_user_was_not_found(
        self, update_user_profile_instance, mocked_users
    ):
        userIdMock = uuid4()

        # Mock behavior of Users repository
        mocked_users.getById.return_value = None

        with pytest.raises(UserWasNotFound):
            update_user_profile_instance.handle(
                userId=str(userIdMock),
                bio=fake.text(),
                birthdate=fake.date_of_birth().strftime("%d/%m/%Y"),
                profilePicUrl=fake.image_url(),
                socialLinks={"github": fake.url()},
            )
