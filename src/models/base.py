from datetime import datetime
from typing import Any
from sqlalchemy.orm import Mapped, mapped_column
import uuid

from src.core.db import db

def generate_uuid() -> str:
    return str(uuid.uuid4())

class UUIDMixin:
    uuid: Mapped[str] = mapped_column(
        db.String(36),
        primary_key=True,
        default=generate_uuid
    )

class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        db.DateTime,
        default=datetime.now,
        nullable=False
    )
    done_at: Mapped[datetime] = mapped_column(
        db.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False
    )

# Base = declarative_base() class User(Base) -> db.Model
class BaseModel(db.Model, UUIDMixin, TimestampMixin):
    __abstract__ = True

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} id={self.id}>"

    def to_dict(self) -> dict[str, Any]:
        # [i for i in range(10)]
        # (i for i in range(10))
        # "i for i in range(10)"
        # {i: f"{i*2}" for i in range(10)}
        return {
            col.name: getattr(self, col.name)
            for col in self.__table__.columns
        }