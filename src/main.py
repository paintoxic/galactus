from packages.logger import init
_LOGGER = init(__name__)


def _load_configs():
    _LOGGER.info("Load configurations")
    from dotenv import load_dotenv
    load_dotenv()


def _connections():
    _LOGGER.info("Starting BackEnd connections")
    from connections import start_connections
    start_connections()


def _start_fastapi():
    _LOGGER.info("Starting Fast API")
    from packages.web.app import start_app
    return start_app()


def main():
    _load_configs()
    _connections()
    return _start_fastapi()


if __name__ == '__main__':
    main()
