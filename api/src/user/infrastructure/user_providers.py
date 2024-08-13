from dependency_injector import containers, providers
from dotenv import load_dotenv

from .repository.mongo_user_repository import MongoUserRepository

load_dotenv()


class UserProviders(containers.DeclarativeContainer):

    USERS = providers.Factory(MongoUserRepository)
