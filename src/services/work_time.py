from typing import List, Dict, Any, Union

from src.repositories.task import TaskRepository

from src.dto import (
    TaskRequestDTO,
    TaskResponseDTO
)

class WorkTimeService:

    def __init__(self):
        self.task_repository = TaskRepository()

    def get_work_times(self):
        return self.task_repository.get_all()
