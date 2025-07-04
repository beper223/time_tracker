from datetime import datetime
from typing import Optional
from pydantic import Field, field_validator, ValidationError

from src.dto.base import (
    BaseDTO,
    IdDTOMixin,
    TimestampDTOMixin
)

class TaskRequestDTO(BaseDTO):
    title: str = Field(
        min_length=15,
        max_length=120
    )
    description: Optional[str] = Field(
        default=None,
        max_length=800
    )
    start_date: datetime
    end_date: datetime
    is_active: bool = True
    is_anonymous: bool = True
    category_id: Optional[int] = None
    # options: list[PollOptionRequestDTO] = Field(
    #     min_length=2
    # )

class TaskResponseDTO(BaseDTO, IdDTOMixin, TimestampDTOMixin):
    title: str
    description: Optional[str]
    start_date: datetime
    end_date: datetime
    is_active: bool
    is_anonymous: bool
    category_id: Optional[int]
    # options: list[PollOptionResponseDTO] = Field(
    #     default_factory=list
    # )