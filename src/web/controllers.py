from flask import jsonify, request
from http import HTTPStatus

from src.services.work_time import WorkTimeService

class WorkTimeController:

    def __init__(self):
        self.work_time_service = WorkTimeService()

    def get_work_times(self):
        result = self.work_time_service.get_work_times()

        return jsonify({
            'status': 'success',
            'data': result,
            'count': len(result)
        }), HTTPStatus.OK