from flask import Blueprint
from src.web.controllers import TaskController

tasks_blueprint = Blueprint(
    'web',
    __name__,
    url_prefix="/"
)

task_controller = TaskController()

tasks_blueprint.add_url_rule(
    '',
    view_func=task_controller.get_tasks,
    methods=['GET']
)
