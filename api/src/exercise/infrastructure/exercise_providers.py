from dependency_injector import containers, providers
from dotenv import load_dotenv

from .repository.mongo_exercise_repository import MongoExerciseRepository

load_dotenv()


class ExerciseProviders(containers.DeclarativeContainer):

    EXERCISES = providers.Factory(MongoExerciseRepository)
