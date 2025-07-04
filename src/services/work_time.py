from typing import List, Dict, Any, Union

from src.repositories.task import TaskRepository

from src.dto import (
    TaskRequestDTO,
    TaskResponseDTO
)

class WorkTimeService:

    def __init__(self):
        self.poll_repository = TaskRepository()