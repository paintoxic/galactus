from os import getenv
from domain.common.adapters.repository import Repository
from packages.storage.mongo import CONNECTIONS
from packages.storage.mongo.implementations.repositories.schemas import SchemasMongoImplementation
from packages.storage.mongo.implementations.repositories.services import ServicesMongoImplementation
from .use_cases.create_one import CreateOne
from .use_cases.get_and_count import GetAndCount

_CONNECTION_KEY = getenv("DB_CONNECTION_KEY", 'my-app')
_DB_NAME = getenv("DB_NAME", 'database')

_CLIENT = CONNECTIONS.get(_CONNECTION_KEY)

_DATABASE = _CLIENT.get_database(_DB_NAME)

repository = Repository(ServicesMongoImplementation(_DATABASE))
schemes_repository = Repository(SchemasMongoImplementation(_DATABASE))

create_one = CreateOne(repository, schemes_repository).execute
get_and_count = GetAndCount(repository).execute
