from flask import Flask

from src.api.routes.work_time import work_time_blueprint


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(work_time_blueprint)