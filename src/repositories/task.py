from typing import List, Union
from sqlalchemy.exc import SQLAlchemyError

from src.core.db import db
from src.models.task import Task
from src.repositories.base import BaseRepository
from src.core.exceptions import (
    TaskCreationException,
)


class TaskRepository(BaseRepository):

    def __init__(self):
        super().__init__(Task)

