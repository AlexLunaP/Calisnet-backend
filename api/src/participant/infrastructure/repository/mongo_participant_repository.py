import os
from typing import List

import pymongo

from ....shared.domain.competition_id import CompetitionId
from ...application.participant_dto import ParticipantDTO
from ...domain.model.participant import Participant
from ...domain.model.participant_id import ParticipantId
from ...domain.repository.participants import Participants


class MongoParticipantRepository(Participants):
    def __init__(self):
        self.__db = pymongo.MongoClient(os.environ["MONGODB_URL"])[
            os.environ["MONGODB_DBNAME"]
        ]
        self.__participants = self.__db["participants"]

    def save(self, participant) -> None:
        self.__participants.insert_one(
            {
                "participant_id": str(participant.participant_id),
                "competition_id": str(participant.competition_id),
                "name": str(participant.name),
            }
        )

    def delete_participant(self, participant: Participant) -> None:
        self.__participants.delete_one(
            {
                "participant_id": str(participant.participant_id),
                "competition_id": str(participant.competition_id),
            }
        )

    def get_by_competition_id(
        self, competition_id: CompetitionId
    ) -> List[ParticipantDTO] | None:

        participants = self.__participants.find(
            {"competition_id": str(competition_id.value)}
        )

        if not participants:
            return None

        participant_list: List[ParticipantDTO] = []

        for participant in participants:
            participant_list.append(
                ParticipantDTO(
                    participant_id=participant["participant_id"],
                    competition_id=participant["competition_id"],
                    name=participant["name"],
                )
            )
        return participant_list

    def get_by_participant_id(
        self, participant_id: ParticipantId
    ) -> List[ParticipantDTO] | None:
        participants = self.__participants.find(
            {"participant_id": str(participant_id.value)}
        )
        if not participants:
            return None

        participant_list: List[ParticipantDTO] = []

        for participant in participants:
            participant_list.append(
                ParticipantDTO(
                    participant_id=participant["participant_id"],
                    competition_id=participant["competition_id"],
                    name=participant["name"],
                )
            )
        return participant_list
