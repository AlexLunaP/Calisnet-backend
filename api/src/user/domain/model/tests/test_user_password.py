import bcrypt

from ..user_password import UserPassword


class TestUserPassword:

    def test_constructor(self):
        password = UserPassword("password")

        assert bcrypt.checkpw("password".encode("utf-8"), password.value)

    def test_from_string_constructor(self):
        password = UserPassword.from_string("password")

        assert bcrypt.checkpw("password".encode("utf-8"), password.value)

    def test_from_hash_constructor(self):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw("password".encode("utf-8"), salt)

        password = UserPassword.from_hash(hashed_password)

        assert bcrypt.checkpw("password".encode("utf-8"), password.value)
