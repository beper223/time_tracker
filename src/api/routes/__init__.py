from flask import Flask
from src.api.routes.work_time import api_blueprint


def register_api_routes(app: Flask) -> None:
    app.register_blueprint(api_blueprint)