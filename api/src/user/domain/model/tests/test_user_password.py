import bcrypt
import pytest

from ..user_password import UserPassword


class TestUserPassword:

    def test_constructor(self):
        password = UserPassword("password")

        assert bcrypt.checkpw("password".encode("utf-8"), password.value)

    def test_from_string_constructor(self):
        password = UserPassword.fromString("password")

        assert bcrypt.checkpw("password".encode("utf-8"), password.value)

    def test_from_hash_constructor(self):
        salt = bcrypt.gensalt()
        hashedPassword = bcrypt.hashpw("password".encode("utf-8"), salt)

        password = UserPassword.fromHash(hashedPassword)

        assert bcrypt.checkpw("password".encode("utf-8"), password.value)
