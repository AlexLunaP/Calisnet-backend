from uuid import uuid4

import faker
import pytest
from pytest_mock import MockerFixture

from .....shared.domain.user_id import UserId
from ....domain.exceptions.user_was_not_found import UserWasNotFound
from ....domain.model.full_name import FullName
from ....domain.model.user_email import UserEmail
from ....domain.model.user_password import UserPassword
from ....domain.model.username import Username
from ....domain.repository.users import User, Users
from ..update_user_profile import UpdateUserProfile

fake = faker.Faker()


@pytest.fixture
def mocked_users(mocker: MockerFixture):
    return mocker.Mock(spec=Users)


@pytest.fixture
def update_user_profile_instance(mocked_users):
    return UpdateUserProfile(users=mocked_users)


class TestUpdateUserProfile:

    def test_update_user_profile(self, update_user_profile_instance, mocked_users):
        user_id_mock = uuid4()

        # Mock behavior of Users repository
        mocked_users.get_by_id.return_value = User(
            user_id=UserId(user_id_mock),
            username=Username(fake.first_name()),
            full_name=FullName(fake.first_name()),
            user_email=UserEmail(fake.email()),
            user_password=UserPassword(fake.password()),
        )

        mocked_profile_image_url = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA..."

        update_user_profile_instance.handle(
            user_id=str(user_id_mock),
            full_name=fake.first_name(),
            bio=fake.text(),
            social_links={"instagram": fake.url()},
            profile_image_url=mocked_profile_image_url,
        )

        mocked_users.update_user_profile.assert_called_once()

    def test_do_not_update_user_profile_if_user_was_not_found(
        self, update_user_profile_instance, mocked_users
    ):
        user_id_mock = uuid4()

        # Mock behavior of Users repository
        mocked_users.get_by_id.return_value = None

        with pytest.raises(UserWasNotFound):
            update_user_profile_instance.handle(
                user_id=str(user_id_mock),
                full_name=fake.first_name(),
                bio=fake.text(),
                social_links={"instagram": fake.url()},
                profile_image_url=fake.image_url(),
            )
