import re
from datetime import timedelta as Timedelta


class ResultTime:

    def __init__(self, result_time: Timedelta):
        self.__value: Timedelta = result_time

    @staticmethod
    def from_string(result_time: str):
        # Parse the string to extract minutes and seconds
        pattern = re.compile(r"(\d+):(\d+)")
        match = pattern.match(result_time)
        if not match:
            raise ValueError("Invalid time format. Expected format: 'MM:SS'")

        minutes = int(match.group(1))
        seconds = int(match.group(2))

        return ResultTime(Timedelta(minutes=minutes, seconds=seconds))

    @property
    def value(self):
        return self.__value

    def validate_result_time(self, result_time: Timedelta):
        if not isinstance(result_time, Timedelta):
            raise TypeError("Result time must be an Timedelta instance")
