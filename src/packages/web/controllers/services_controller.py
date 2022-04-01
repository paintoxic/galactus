from domain.services import create_one, get_and_count
from domain.services.models.service_dom import ServiceDOM
from packages.web.models.scheme_api import SchemesAPI


class ServicesController(object):
    def __init__(self):
        pass

    def create(self, item: SchemesAPI):
        entity = ServiceDOM(item.dict())
        return create_one(entity)

    def get_all(self):
        return get_and_count()
