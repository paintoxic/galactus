
from logging import Filter, getLogger
from os import getenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run, config

_DEVELOPMENT_ENV = 'development'
_ASGI_ENV = getenv('ASGI_ENV', _DEVELOPMENT_ENV)


class Unless(Filter):
    def filter(self, record) -> bool:
        _, method, path, _, _ = record.args
        return method == 'GET' and not path in [
            "/",
            "/healthy",
            "/liveness",
            "/docs",
            "/openapi.json"
        ]


def _launch_asgi_server(app: FastAPI):
    log_config = config.LOGGING_CONFIG
    log_config["formatters"]["access"]["fmt"] = "[%(asctime)s] - %(levelname)s - %(client_addr)s - %(request_line)s %(status_code)s "
    log_config["formatters"]["default"]["fmt"] = "[%(asctime)s] - %(levelname)s - %(message)s"

    _PORT = int(getenv("PORT", "3000"))
    _HOST = getenv("HOST", "0.0.0.0")

    getLogger("uvicorn.access").addFilter(Unless())
    run(app, host=_HOST, port=_PORT, log_config=log_config)


def start_app():
    from packages.web.routes import routes

    tags_metadata = [
        {
            "name": "healthy",
            "description": "Routes to inform the healthy of service",
        },
    ]

    app = FastAPI(title="Deployer", openapi_tags=tags_metadata)

    app.add_middleware(
        CORSMiddleware,
        allow_origins="*",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(routes)
    if(_ASGI_ENV != _DEVELOPMENT_ENV):
        _launch_asgi_server(app)
    return app
