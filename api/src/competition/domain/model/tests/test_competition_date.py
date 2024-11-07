from datetime import datetime

from faker import Faker

from ..competition_date import CompetitionDate

fake = Faker()


class TestCompetitionDate:

    def test_costructor(self):
        expected_value = fake.future_datetime()

        competition_date = CompetitionDate(expected_value)

        assert competition_date.value == expected_value

    def test_from_string_constructor(self):
        expected_value = fake.future_datetime().strftime("%Y-%m-%d")

        competition_date = CompetitionDate.from_string(expected_value)

        assert competition_date.value == datetime.strptime(expected_value, "%Y-%m-%d")

    def test_from_datetime_constructor(self):
        expected_value = fake.future_datetime()

        competition_date = CompetitionDate.from_datetime(expected_value)

        assert competition_date.value == expected_value
