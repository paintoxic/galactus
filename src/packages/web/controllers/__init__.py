from .healthy_controller import HealthyController
from .schemes_controller import SchemesController
from .services_controller import ServicesController
from os import getenv

healthy_controller = HealthyController(getenv)
schemes_controller = SchemesController()
services_controller = ServicesController()
