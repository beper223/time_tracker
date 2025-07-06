from flask import Flask
from src.web.routes.main import tasks_blueprint


def register_web_routes(app: Flask) -> None:
    app.register_blueprint(tasks_blueprint)