from uuid import UUID


class UserId:

    def __init__(self, user_id: UUID):
        self.validate_user_id(user_id)
        self.__value: UUID = user_id

    @staticmethod
    def from_string(user_id: str):
        return UserId(UUID(user_id))

    @property
    def value(self):
        return self.__value

    def validate_user_id(self, user_id: UUID):
        if not isinstance(user_id, UUID):
            raise TypeError("User ID must be an UUID instance")
