from flask import Flask, Blueprint
from src.web.controllers import WorkTimeController
#from src.core.config import settings

tasks_blueprint = Blueprint(
    'web',
    __name__,
    url_prefix="/"
)

work_time_controller = WorkTimeController()

tasks_blueprint.add_url_rule(
    '',
    view_func=work_time_controller.get_work_times,
    methods=['GET']
)

def register_web_routes(app: Flask) -> None:
    app.register_blueprint(tasks_blueprint)