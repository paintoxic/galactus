from packages.logger import init
from os import getenv
from time import sleep

_LOGGER = init(__name__)


def _db_connection(retry_times_counter=0):
    from packages.storage.mongo import check_connection, connect

    retry_times = int(getenv("DB_RETRY_TIMES", '5'))
    retry_connection_timeout = int(getenv("DB_RETRY_TIMEOUT_SECS", '5'))
    db_uri = getenv("MONGO_URI", 'mongodb://localhost:27030')
    connection_key = getenv("DB_CONNECTION_KEY", 'my-app')
    try:
        _LOGGER.debug("Checking DB connection...")
        connect(db_uri, connection_key)
        check_connection(connection_key)
        _LOGGER.debug("DB connection is already fine.")
    except Exception as e:
        retry_times_counter += 1
        _LOGGER.debug(
            f"Retry times limit: {retry_times}, retry counter: {retry_times_counter}")
        if retry_times_counter < retry_times:
            _LOGGER.warning(
                f"Retrying connection to DB in {retry_connection_timeout} secs")
            sleep(retry_connection_timeout)
            return _db_connection(retry_times_counter)
        else:
            _LOGGER.critical(
                "Critical error connecting to DB: {}, ex: {}".format(db_uri, e))
            raise


def start_connections():
    _db_connection()
