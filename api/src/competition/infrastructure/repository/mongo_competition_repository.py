import os
from typing import List, Optional

import pymongo

from ....shared.domain.competition_id import CompetitionId
from ....shared.domain.user_id import UserId
from ...application.competition_dto import CompetitionDTO
from ...domain.model.competition import Competition
from ...domain.model.competition_date import CompetitionDate
from ...domain.model.competition_description import CompetitionDescription
from ...domain.model.competition_image_url import CompetitionImageUrl
from ...domain.model.competition_location import CompetitionLocation
from ...domain.model.competition_name import CompetitionName
from ...domain.model.competition_status import CompetitionStatus
from ...domain.model.participant_limit import ParticipantLimit
from ...domain.model.penalty_time import PenaltyTime
from ...domain.repository.competitions import Competitions


class MongoCompetitionRepository(Competitions):
    def __init__(self):
        self.__db = pymongo.MongoClient(os.environ["MONGODB_URL"])[
            os.environ["MONGODB_DBNAME"]
        ]
        self.__competitions = self.__db["competitions"]

    def save(self, competition: Competition) -> None:
        self.__competitions.insert_one(
            {
                "competition_id": str(competition.competition_id),
                "organizer_id": str(competition.organizer_id),
                "name": str(competition.name),
                "description": str(competition.description),
                "date": str(competition.date.value),
                "location": str(competition.location),
                "image": str(competition.image),
                "participant_limit": competition.participant_limit,
                "penalty_time": competition.penalty_time,
                "status": str(competition.status),
            }
        )

    def get_by_id(self, competition_id: CompetitionId) -> Optional[Competition]:
        competition = self.__competitions.find_one(
            {"competition_id": str(competition_id.value)}
        )
        if not competition:
            return None

        return self._get_competition_from_result(competition)

    def get_all(self) -> List[CompetitionDTO] | None:
        competitions = self.__competitions.find().sort("date", pymongo.DESCENDING)

        if not competitions:
            return None

        competitions_list: List[CompetitionDTO] = []

        for competition in competitions:
            competitions_list.append(
                CompetitionDTO(
                    competition_id=competition["competition_id"],
                    organizer_id=competition["organizer_id"],
                    name=competition["name"],
                    description=competition["description"],
                    date=competition["date"],
                    location=competition["location"],
                    image=competition["image"],
                    participant_limit=competition["participant_limit"],
                    penalty_time=competition["penalty_time"],
                    status=competition["status"],
                )
            )

        return competitions_list

    def get_by_status(self, competition_status: str) -> List[CompetitionDTO] | None:
        competitions = self.__competitions.find(
            {"status": {"$regex": f"^{competition_status}$", "$options": "i"}}
        ).sort("date", pymongo.DESCENDING)

        if not competitions:
            return None

        competitions_list: List[CompetitionDTO] = []

        for competition in competitions:
            competitions_list.append(
                CompetitionDTO(
                    competition_id=competition["competition_id"],
                    organizer_id=competition["organizer_id"],
                    name=competition["name"],
                    description=competition["description"],
                    date=competition["date"],
                    location=competition["location"],
                    image=competition["image"],
                    participant_limit=competition["participant_limit"],
                    penalty_time=competition["penalty_time"],
                    status=competition["status"],
                )
            )
        return competitions_list

    def get_by_organizer_id(self, organizer_id: UserId) -> List[CompetitionDTO] | None:

        competitions = self.__competitions.find(
            {"organizer_id": str(organizer_id.value)}
        ).sort("date", pymongo.DESCENDING)

        if not competitions:
            return None

        competitions_list: List[CompetitionDTO] = []

        for competition in competitions:
            competitions_list.append(
                CompetitionDTO(
                    competition_id=competition["competition_id"],
                    organizer_id=competition["organizer_id"],
                    name=competition["name"],
                    description=competition["description"],
                    date=competition["date"],
                    location=competition["location"],
                    image=competition["image"],
                    participant_limit=competition["participant_limit"],
                    penalty_time=competition["penalty_time"],
                    status=competition["status"],
                )
            )
        return competitions_list

    def update_competition(self, competition: Competition) -> None:
        self.__competitions.update_one(
            {"competition_id": str(competition.competition_id)},
            {
                "$set": {
                    "name": str(competition.name),
                    "description": str(competition.description),
                    "date": str(competition.date.value),
                    "location": str(competition.location),
                    "image": str(competition.image),
                    "participant_limit": competition.participant_limit,
                    "penalty_time": competition.penalty_time,
                    "status": str(competition.status),
                }
            },
        )

    def _get_competition_from_result(self, result) -> Competition:
        return Competition(
            competition_id=CompetitionId.from_string((result["competition_id"])),
            organizer_id=UserId.from_string((result["organizer_id"])),
            name=CompetitionName.from_string((result["name"])),
            description=CompetitionDescription.from_string((result["description"])),
            date=CompetitionDate.from_string((result["date"])),
            location=CompetitionLocation.from_string((result["location"])),
            image=CompetitionImageUrl.from_string((result["image"])),
            participant_limit=ParticipantLimit((result["participant_limit"])),
            penalty_time=PenaltyTime((result["penalty_time"])),
            status=CompetitionStatus.from_string((result["status"])),
        )
