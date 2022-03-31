from domain.schemes.models.scheme_dom import SchemesDOM
from domain.schemes import create_one, get_and_count
from packages.web.models.scheme_api import SchemesAPI


class SchemesController(object):
    def __init__(self):
        pass

    def create(self, item: SchemesAPI):
        entity = SchemesDOM(item.dict())
        return create_one(entity)

    def get_all(self):
        return get_and_count()
