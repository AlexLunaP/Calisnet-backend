from dependency_injector import containers, providers
from dotenv import load_dotenv

from .repository.mongo_competition_repository import MongoCompetitionRepository

load_dotenv()


class CompetitionProviders(containers.DeclarativeContainer):

    COMPETITIONS = providers.Factory(MongoCompetitionRepository)
