from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import BaseModel
from src.core.db import db


class Task(BaseModel):
    __tablename__ = "tasks"

    title: Mapped[str] = mapped_column(
        db.String(120),
        nullable=False
    )