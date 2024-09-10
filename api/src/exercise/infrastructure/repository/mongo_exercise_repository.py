import os
from typing import List, Optional

import pymongo

from ....shared.domain.competition_id import CompetitionId
from ...application.exercise_dto import ExerciseDTO
from ...domain.model.execution_order import ExecutionOrder
from ...domain.model.exercise import Exercise
from ...domain.model.exercise_id import ExerciseId
from ...domain.model.exercise_name import ExerciseName
from ...domain.model.exercise_reps import ExerciseReps
from ...domain.model.exercise_sets import ExerciseSets
from ...domain.repository.exercises import Exercises


class MongoExerciseRepository(Exercises):
    def __init__(self):
        self.__db = pymongo.MongoClient(os.environ["MONGODB_URL"])[
            os.environ["MONGODB_DBNAME"]
        ]
        self.__exercises = self.__db["exercises"]

    def save(self, exercise) -> None:
        self.__exercises.insert_one(
            {
                "exercise_id": str(exercise.exercise_id),
                "competition_id": str(exercise.competition_id),
                "name": str(exercise.name),
                "sets": exercise.sets,
                "reps": exercise.reps,
                "execution_order": exercise.execution_order,
            }
        )

    def get_by_id(self, exercise_id) -> Optional[Exercise]:
        exercise = self.__exercises.find_one({"exercise_id": str(exercise_id.value)})

        if not exercise:
            return None

        return self._get_exercise_from_result(exercise)

    def get_by_competition_id(
        self, competition_id: CompetitionId
    ) -> List[ExerciseDTO] | None:

        exercises = self.__exercises.find(
            {"competition_id": str(competition_id.value)}
        ).sort("execution_order", pymongo.ASCENDING)

        if not exercises:
            return None

        exercises_list: List[ExerciseDTO] = []

        for exercise in exercises:
            exercises_list.append(
                ExerciseDTO(
                    exercise_id=exercise["exercise_id"],
                    competition_id=exercise["competition_id"],
                    name=exercise["name"],
                    sets=exercise["sets"],
                    reps=exercise["reps"],
                    execution_order=exercise["execution_order"],
                )
            )
        return exercises_list

    def _get_exercise_from_result(self, result) -> Exercise:
        return Exercise(
            exercise_id=ExerciseId.from_string(result["exercise_id"]),
            competition_id=CompetitionId.from_string(result["competition_id"]),
            name=ExerciseName.from_string(result["name"]),
            sets=ExerciseSets(result["sets"]),
            reps=ExerciseReps(result["reps"]),
            execution_order=ExecutionOrder(result["execution_order"]),
        )
