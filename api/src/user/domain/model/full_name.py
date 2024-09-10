class FullName:
    class InvalidFullName(Exception):
        pass

    def __init__(self, full_name: str):
        self.__validate_full_name_not_empty(full_name)
        self.__full_name: str = full_name

    @staticmethod
    def from_string(full_name: str):
        return FullName(full_name)

    @property
    def value(self):
        return self.__full_name

    def __validate_full_name_not_empty(self, full_name: str):
        if len(full_name) == 0:
            raise self.InvalidFullName("Full name cannot be empty")
