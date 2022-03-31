from .healthy_controller import HealthyController
from .schemes_controller import SchemesController
from os import getenv

healthy_controller = HealthyController(getenv)
schemes_controller = SchemesController()
