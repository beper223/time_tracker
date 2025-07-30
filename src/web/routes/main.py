from flask import Blueprint
from src.web.controllers import TaskController

tasks_blueprint = Blueprint(
    'web',
    __name__,
    template_folder='templates'
)

task_controller = TaskController()

tasks_blueprint.add_url_rule(
    '',
    view_func=task_controller.task_list,
    methods=['GET']
)
tasks_blueprint.add_url_rule(
    '/new',
    view_func=task_controller.new_task,
    methods=['GET']
)
