from flask import Blueprint

from src.api.controllers.work_time import WorkTimeController
from src.core.config import settings


api_blueprint = Blueprint(
    'api',
    __name__,
    url_prefix=f"{settings.API_PREFIX}/{settings.API_VERSION}/tasks"
)

api_controller = WorkTimeController()

api_blueprint.add_url_rule(
    '',
    view_func=api_controller.get_work_times,
    methods=['GET']
)