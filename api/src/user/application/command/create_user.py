from ....shared.domain.user_id import UserId
from ...domain.exceptions.user_email_already_exists import UserEmailAlreadyExists
from ...domain.exceptions.user_id_already_exists import UserIdAlreadyExists
from ...domain.exceptions.username_already_exists import UserNameAlreadyExists
from ...domain.model.full_name import FullName
from ...domain.model.user import User
from ...domain.model.user_email import UserEmail
from ...domain.model.user_password import UserPassword
from ...domain.model.username import Username
from ...domain.repository.users import Users


class CreateUser:

    def __init__(self, users: Users):
        self.users = users

    def handle(self, user_id: str, username: str, user_email: str, user_password: str):
        user_id_object = UserId.from_string(user_id)
        username_object = Username.from_string(username)
        full_name_object = FullName.from_string(username)
        user_email_object = UserEmail.from_string(user_email)

        if self.users.get_by_id(user_id_object):
            raise UserIdAlreadyExists("The user ID already exists")

        if self.users.get_by_username(username_object):
            raise UserNameAlreadyExists("The username already exists")

        if self.users.get_by_email(user_email_object):
            raise UserEmailAlreadyExists("The user email already exists")

        user = User.add(
            user_id=user_id_object,
            username=username_object,
            user_email=user_email_object,
            user_password=UserPassword.from_string(user_password),
            full_name=full_name_object,
        )

        self.users.save(user)
