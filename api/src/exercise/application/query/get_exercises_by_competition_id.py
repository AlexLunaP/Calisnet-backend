from typing import List, Optional

from ....shared.domain.competition_id import CompetitionId
from ...application.exercise_dto import ExerciseDTO
from ...domain.repository.exercises import Exercises
from .get_exercises_by_competition_id_response import (
    GetExercisesByCompetitionIdResponse,
)


class GetExercisesByCompetitionIdQuery:
    def __init__(self, competition_id: str):
        self.__competition_id: str = competition_id

    @property
    def competition_id(self):
        return self.__competition_id


class GetExercisesByCompetitionIdHandler:
    def __init__(self, exercises: Exercises):
        self.__exercises = exercises

    def handle(
        self, query: GetExercisesByCompetitionIdQuery
    ) -> Optional[GetExercisesByCompetitionIdResponse]:
        competition_id = CompetitionId.from_string(query.competition_id)

        exercises: List[ExerciseDTO] | None = self.__exercises.get_by_competition_id(
            competition_id
        )

        if not exercises:
            return None

        get_exercises_by_competition_id_response = GetExercisesByCompetitionIdResponse(
            exercises
        )

        return get_exercises_by_competition_id_response
