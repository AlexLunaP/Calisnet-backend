from uuid import uuid4

import faker
import pytest
from pytest_mock import MockerFixture

from .....shared.domain.competition_id import CompetitionId
from .....shared.domain.user_id import UserId
from ....domain.exceptions.competition_was_not_found import CompetitionWasNotFound
from ....domain.model.competition import Competition
from ....domain.model.competition_date import CompetitionDate
from ....domain.model.competition_description import CompetitionDescription
from ....domain.model.competition_image_url import CompetitionImageUrl
from ....domain.model.competition_location import CompetitionLocation
from ....domain.model.competition_name import CompetitionName
from ....domain.model.competition_status import CompetitionStatus
from ....domain.model.participant_limit import ParticipantLimit
from ....domain.model.penalty_time import PenaltyTime
from ....domain.repository.competitions import Competitions
from ..update_competition import UpdateCompetition

fake = faker.Faker()


@pytest.fixture
def mocked_competitions(mocker: MockerFixture):
    return mocker.Mock(spec=Competitions)


@pytest.fixture
def create_competition_instance(mocked_competitions):
    return UpdateCompetition(competitions=mocked_competitions)


class TestUpdateCompetition:

    def test_update_competition(self, create_competition_instance, mocked_competitions):
        competition_id_mock = uuid4()

        # Mock behavior of Competitions repository
        mocked_competitions.get_by_id.return_value = Competition(
            competition_id=CompetitionId(competition_id_mock),
            organizer_id=UserId(uuid4()),
            name=CompetitionName(fake.name()),
            description=CompetitionDescription(fake.text()),
            date=CompetitionDate.from_string(
                fake.future_datetime().strftime("%Y-%m-%d")
            ),
            location=CompetitionLocation(fake.address()),
            image=CompetitionImageUrl(fake.url()),
            participant_limit=ParticipantLimit(10),
            penalty_time=PenaltyTime(10),
            status=CompetitionStatus.OPEN,
        )

        create_competition_instance.handle(
            competition_id=str(competition_id_mock),
            name=fake.name(),
            description=fake.text(),
            date=fake.future_datetime().strftime("%Y-%m-%d"),
            location=fake.address(),
            image=fake.url(),
            participant_limit=10,
            penalty_time=10,
            status=CompetitionStatus.OPEN.value,
        )

        mocked_competitions.update_competition.assert_called_once()

    def test_do_not_update_competition_if_competition_was_not_found(
        self, create_competition_instance, mocked_competitions
    ):
        competition_id_mock = uuid4()

        # Mock behavior of Competitions repository
        mocked_competitions.get_by_id.return_value = None

        with pytest.raises(CompetitionWasNotFound):
            create_competition_instance.handle(
                competition_id=str(competition_id_mock),
                name=fake.name(),
                description=fake.text(),
                date=fake.future_datetime().strftime("%Y-%m-%d"),
                location=fake.address(),
                image=fake.url(),
                participant_limit=10,
                penalty_time=10,
                status=CompetitionStatus.OPEN.value,
            )
