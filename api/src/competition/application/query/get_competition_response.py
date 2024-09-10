from ..competition_dto import CompetitionDTO


class GetCompetitionResponse:
    def __init__(
        self,
        competition_id: str,
        organizer_id: str,
        name: str,
        description: str,
        date: str,
        location: str,
        image: str,
        participant_limit: int,
        penalty_time: int,
        status: str,
    ):
        self.__competition_id: str = competition_id
        self.__organizer_id: str = organizer_id
        self.__name: str = name
        self.__description: str = description
        self.__date: str = date
        self.__location: str = location
        self.__image: str = image
        self.__participant_limit: int = participant_limit
        self.__penalty_time: int = penalty_time
        self.__status: str = status

    @property
    def competition_id(self):
        return self.__competition_id

    @property
    def organizer_id(self):
        return self.__organizer_id

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def date(self):
        return self.__date

    @property
    def location(self):
        return self.__location

    @property
    def image(self):
        return self.__image

    @property
    def participant_limit(self):
        return self.__participant_limit

    @property
    def penalty_time(self):
        return self.__penalty_time

    @property
    def status(self):
        return self.__status

    @property
    def competition_dto(self):
        return CompetitionDTO(
            competition_id=self.competition_id,
            organizer_id=self.organizer_id,
            name=self.name,
            description=self.description,
            date=self.date,
            location=self.location,
            image=self.image,
            participant_limit=self.participant_limit,
            penalty_time=self.penalty_time,
            status=self.status,
        )
