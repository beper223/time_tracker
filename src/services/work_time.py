from typing import List, Dict, Any, Union

from src.repositories.tasks import TasksRepository

from src.dto import (
    TasksRequestDTO,
    TasksResponseDTO
)

class WorkTimeService:

    def __init__(self):
        self.poll_repository = TasksRepository()