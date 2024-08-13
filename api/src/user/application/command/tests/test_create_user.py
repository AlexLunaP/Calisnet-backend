from uuid import UUID, uuid4

import faker
import pytest
from pytest_mock import mocker

from .....shared.domain.user_id import UserId
from ....domain.exception.user_email_already_exists import UserEmailAlreadyExists
from ....domain.exception.user_id_already_exists import UserIdAlreadyExists
from ....domain.exception.username_already_exists import UserNameAlreadyExists
from ....domain.model.user_email import UserEmail
from ....domain.model.user_password import UserPassword
from ....domain.model.username import Username
from ....domain.repository.users import User, Users
from ..create_user import CreateUser

fake = faker.Faker()


@pytest.fixture
def mocked_users(mocker):
    return mocker.Mock(spec=Users)


@pytest.fixture
def create_user_instance(mocked_users):
    return CreateUser(users=mocked_users)


class TestCreateUser:

    def test_create_a_new_user(self, create_user_instance, mocked_users):

        # Mock behavior of Users repository
        mocked_users.getById.return_value = None
        mocked_users.getByUsername.return_value = None
        mocked_users.getByEmail.return_value = None

        create_user_instance.handle(
            userId=str(uuid4()),
            username=fake.first_name(),
            userEmail=fake.email(),
            userPassword=fake.password(),
        )
        mocked_users.save.assert_called_once()

    def test_do_not_create_user_if_user_id_already_exists(
        self, create_user_instance, mocked_users
    ):

        # Mock behavior of Users repository to return a user with the same ID
        mocked_users.getById.return_value = User(
            userId=UserId.fromString(str(uuid4())),
            username=Username.fromString(fake.first_name()),
            userEmail=UserEmail.fromString(fake.email()),
            userPassword=UserPassword.fromString(fake.password()),
        )

        with pytest.raises(UserIdAlreadyExists):
            create_user_instance.handle(
                userId=str(uuid4()),
                username=fake.first_name(),
                userEmail=fake.email(),
                userPassword=fake.password(),
            )

    def test_do_not_create_user_if_username_already_exists(
        self, create_user_instance, mocked_users
    ):
        mocked_users.getById.return_value = None

        mocked_users.getByUsername.return_value = User(
            userId=UserId.fromString(str(uuid4())),
            username=Username.fromString(fake.first_name()),
            userEmail=UserEmail.fromString(fake.email()),
            userPassword=UserPassword.fromString(fake.password()),
        )

        with pytest.raises(UserNameAlreadyExists):
            create_user_instance.handle(
                userId=str(uuid4()),
                username=fake.first_name(),
                userEmail=fake.email(),
                userPassword=fake.password(),
            )

    def test_do_not_create_user_if_user_email_already_exists(
        self, create_user_instance, mocked_users
    ):
        mocked_users.getById.return_value = None
        mocked_users.getByUsername.return_value = None

        mocked_users.getByEmail.return_value = User(
            userId=UserId.fromString(str(uuid4())),
            username=Username.fromString(fake.first_name()),
            userEmail=UserEmail.fromString(fake.email()),
            userPassword=UserPassword.fromString(fake.password()),
        )

        with pytest.raises(UserEmailAlreadyExists):
            create_user_instance.handle(
                userId=str(uuid4()),
                username=fake.first_name(),
                userEmail=fake.email(),
                userPassword=fake.password(),
            )
