from src.dto.base import (
    BaseDTO,
    TimestampDTOMixin,
    IdDTOMixin,
    PaginationRequestDTO,
    PaginationResponseDTO
)
from src.dto.task import (
    TaskRequestDTO,
    TaskResponseDTO
)

__all__ = (
    "BaseDTO",
    "TimestampDTOMixin",
    "IdDTOMixin",
    "PaginationRequestDTO",
    "PaginationResponseDTO",

    "TaskRequestDTO",# запрос
    "TaskResponseDTO"# ответ
)