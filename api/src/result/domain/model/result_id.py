from uuid import UUID


class ResultId:

    def __init__(self, result_id: UUID):
        self.validate_result_id(result_id)
        self.__value: UUID = result_id

    @staticmethod
    def from_string(result_id: str):
        return ResultId(UUID(result_id))

    @property
    def value(self):
        return self.__value

    def validate_result_id(self, result_id: UUID):
        if not isinstance(result_id, UUID):
            raise TypeError("Result ID must be an UUID instance")
