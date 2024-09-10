class ExecutionOrder:

    class invalidExecutionOrder(ValueError):
        pass

    def __init__(self, execution_order: int):
        self.__validate_execution_order(execution_order)
        self.__execution_order: int = execution_order

    @staticmethod
    def from_string(execution_order: str):
        return ExecutionOrder(int(execution_order))

    @property
    def value(self):
        return self.__execution_order

    def __validate_execution_order(self, execution_order: int):
        if execution_order < 1:
            raise self.invalidExecutionOrder("Execution order must be greater than 0")
