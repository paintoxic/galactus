source .env
uvicorn --app-dir=src main:main --port $PORT --reload --factory