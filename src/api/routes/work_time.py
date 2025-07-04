from flask import Blueprint

from src.api.controllers.work_time import WorkTimeController
from src.core.config import settings


work_time_blueprint = Blueprint(
    'tasks',
    __name__,
    url_prefix=f"{settings.API_PREFIX}/{settings.API_VERSION}/tasks"
)

work_time_controller = WorkTimeController()

work_time_blueprint.add_url_rule(
    '',
    view_func=work_time_controller.get_work_times,
    methods=['GET']
)