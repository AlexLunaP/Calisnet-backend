from uuid import uuid4

import faker
import pytest
from pytest_mock import MockerFixture

from .....shared.domain.user_id import UserId
from ....domain.exceptions.user_email_already_exists import UserEmailAlreadyExists
from ....domain.exceptions.user_id_already_exists import UserIdAlreadyExists
from ....domain.exceptions.username_already_exists import UserNameAlreadyExists
from ....domain.model.full_name import FullName
from ....domain.model.user_email import UserEmail
from ....domain.model.user_password import UserPassword
from ....domain.model.username import Username
from ....domain.repository.users import User, Users
from ..create_user import CreateUser

fake = faker.Faker()


@pytest.fixture
def mocked_users(mocker: MockerFixture):
    return mocker.Mock(spec=Users)


@pytest.fixture
def create_user_instance(mocked_users):
    return CreateUser(users=mocked_users)


class TestCreateUser:

    def test_create_new_user(self, create_user_instance, mocked_users):

        # Mock behavior of Users repository
        mocked_users.get_by_id.return_value = None
        mocked_users.get_by_username.return_value = None
        mocked_users.get_by_email.return_value = None

        create_user_instance.handle(
            user_id=str(uuid4()),
            username=fake.first_name(),
            user_email=fake.email(),
            user_password=fake.password(),
        )
        mocked_users.save.assert_called_once()

    def test_do_not_create_user_if_user_id_already_exists(
        self, create_user_instance, mocked_users
    ):

        # Mock behavior of Users repository to return a user with the same ID
        mocked_users.get_by_id.return_value = User(
            user_id=UserId.from_string(str(uuid4())),
            username=Username.from_string(fake.first_name()),
            full_name=FullName.from_string(fake.first_name()),
            user_email=UserEmail.from_string(fake.email()),
            user_password=UserPassword.from_string(fake.password()),
        )

        with pytest.raises(UserIdAlreadyExists):
            create_user_instance.handle(
                user_id=str(uuid4()),
                username=fake.first_name(),
                user_email=fake.email(),
                user_password=fake.password(),
            )

    def test_do_not_create_user_if_username_already_exists(
        self, create_user_instance, mocked_users
    ):
        mocked_users.get_by_id.return_value = None

        mocked_users.get_by_username.return_value = User(
            user_id=UserId.from_string(str(uuid4())),
            username=Username.from_string(fake.first_name()),
            full_name=FullName.from_string(fake.first_name()),
            user_email=UserEmail.from_string(fake.email()),
            user_password=UserPassword.from_string(fake.password()),
        )

        with pytest.raises(UserNameAlreadyExists):
            create_user_instance.handle(
                user_id=str(uuid4()),
                username=fake.first_name(),
                user_email=fake.email(),
                user_password=fake.password(),
            )

    def test_do_not_create_user_if_user_email_already_exists(
        self, create_user_instance, mocked_users
    ):
        mocked_users.get_by_id.return_value = None
        mocked_users.get_by_username.return_value = None

        mocked_users.get_by_email.return_value = User(
            user_id=UserId.from_string(str(uuid4())),
            username=Username.from_string(fake.first_name()),
            full_name=FullName.from_string(fake.first_name()),
            user_email=UserEmail.from_string(fake.email()),
            user_password=UserPassword.from_string(fake.password()),
        )

        with pytest.raises(UserEmailAlreadyExists):
            create_user_instance.handle(
                user_id=str(uuid4()),
                username=fake.first_name(),
                user_email=fake.email(),
                user_password=fake.password(),
            )
