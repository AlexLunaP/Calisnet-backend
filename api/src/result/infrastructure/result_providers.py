from dependency_injector import containers, providers
from dotenv import load_dotenv

from .repository.mongo_result_repository import MongoResultRepository

load_dotenv()


class ResultProviders(containers.DeclarativeContainer):

    RESULTS = providers.Factory(MongoResultRepository)
