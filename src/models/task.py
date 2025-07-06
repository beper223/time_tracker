from enum import Enum
from datetime import date, time
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import BaseModel
from src.core.db import db

class TaskType(str, Enum):
    CLEANING = "putzen"
    PLASTERING = "verputzen"

class Task(BaseModel):
    __tablename__ = "tasks"

    description: Mapped[str] = mapped_column(
        db.String(120),
        #nullable=False
    )
    is_closed: Mapped[bool] = mapped_column(
        db.Boolean,
        default=False,
        nullable=False
    )

    task_type: Mapped[str] = mapped_column(
        db.Enum(TaskType, name="task_type_enum"),
        nullable=False,
        #default=TaskType.CLEANING,
        #comment="Тип работ, например 'putzen' или 'verputzen'"
    )

    work_date: Mapped[date] = mapped_column(
        db.Date,
        nullable=False
    )

    start_time: Mapped[time] = mapped_column(
        db.Time,
        nullable=False
    )

    end_time: Mapped[time] = mapped_column(
        db.Time,
        #nullable=False
    )