from os import getenv
from domain.common.adapters.repository import Repository
from packages.storage.mongo import CONNECTIONS
from packages.storage.mongo.implementations.repositories.schemas import SchemasMongoImplementation
from .use_cases.create_one import CreateOne
from .use_cases.get_and_count import GetAndCount
from .use_cases.get_by_id import GetById

_CONNECTION_KEY = getenv("DB_CONNECTION_KEY", 'my-app')
_DB_NAME = getenv("DB_NAME", 'database')

_CLIENT = CONNECTIONS.get(_CONNECTION_KEY)

_DATABASE = _CLIENT.get_database(_DB_NAME)

repository = Repository(SchemasMongoImplementation(_DATABASE))

create_one = CreateOne(repository).execute
get_and_count = GetAndCount(repository).execute
get_by_id = GetById(repository).execute
