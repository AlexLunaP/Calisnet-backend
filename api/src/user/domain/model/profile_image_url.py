class ProfileImageUrl:

    def __init__(self, value: str):
        self.__value = value

    @staticmethod
    def from_string(value: str):
        return ProfileImageUrl(value)

    @property
    def value(self) -> str:
        return self.__value
