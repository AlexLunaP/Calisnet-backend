class Username:
    class InvalidUsername(Exception):
        pass

    def __init__(self, username: str):
        self._validate_username_not_empty(username)
        self._validate_username_spacing(username)
        self._username: str = username

    @staticmethod
    def from_string(username: str):
        return Username(username)

    @property
    def value(self):
        return self._username

    def _validate_username_not_empty(self, username: str):
        if len(username) == 0:
            raise self.InvalidUsername("Username cannot be empty")

    def _validate_username_spacing(self, username: str):
        if " " in username:
            raise self.InvalidUsername("Username cannot have white spaces")
