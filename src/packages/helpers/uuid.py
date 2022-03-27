from uuid import uuid4, UUID


def generate_uuid4():
    return str(uuid4())


def is_valid_uuid_4(id: str):
    try:
        UUID(id)
        return True
    except ValueError:
        return False
