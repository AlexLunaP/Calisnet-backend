from datetime import datetime


class CompetitionDate:

    def __init__(self, competition_date: datetime):
        self.__competition_date: datetime = competition_date

    @staticmethod
    def from_string(competition_date: str):
        parsed_date = datetime.fromisoformat(competition_date)
        return CompetitionDate(parsed_date)

    @staticmethod
    def from_datetime(competition_date: datetime):
        return CompetitionDate(competition_date)

    @property
    def value(self):
        return self.__competition_date

    @property
    def __str__(self):
        return str(self.__competition_date)
