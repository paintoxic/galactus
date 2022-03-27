from .healthy_controller import HealthyController
from os import getenv

healthy_controller = HealthyController(getenv)
