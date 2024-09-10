class Penalties:

    class invalidPenalties(ValueError):
        pass

    def __init__(self, penalties: int):
        self.__validate_penalties(penalties)
        self.__penalties: int = penalties

    @staticmethod
    def from_string(penalties: str):
        return Penalties(int(penalties))

    @property
    def value(self):
        return self.__penalties

    def __validate_penalties(self, penalties: int):
        if penalties < 0:
            raise self.invalidPenalties("Number of penalties cannot be negative")
