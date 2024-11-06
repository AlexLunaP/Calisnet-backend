from abc import ABC, abstractmethod
from typing import List, Optional

from ....shared.domain.competition_id import CompetitionId
from ...application.exercise_dto import ExerciseDTO
from ..model.exercise import Exercise
from ..model.exercise_id import ExerciseId


class Exercises(ABC):

    @abstractmethod
    def save(self, exercise: Exercise) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, exercise_id: ExerciseId) -> Optional[Exercise]:
        raise NotImplementedError

    @abstractmethod
    def get_by_competition_id(
        self, competition_id: CompetitionId
    ) -> Optional[List[ExerciseDTO]]:
        raise NotImplementedError

    @abstractmethod
    def delete_exercise(self, exercise_id: ExerciseId) -> None:
        raise NotImplementedError
