from flask import jsonify, request
from http import HTTPStatus

from src.services.work_time import WorkTimeService

class WorkTimeController:

    def __init__(self):
        self.work_time_service = WorkTimeService()