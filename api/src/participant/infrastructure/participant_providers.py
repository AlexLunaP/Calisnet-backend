from dependency_injector import containers, providers
from dotenv import load_dotenv

from .repository.mongo_participant_repository import MongoParticipantRepository

load_dotenv()


class ParticipantProviders(containers.DeclarativeContainer):

    PARTICIPANTS = providers.Factory(MongoParticipantRepository)
