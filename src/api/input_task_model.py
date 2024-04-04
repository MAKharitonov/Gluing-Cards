from src.api.task import Task
from typing import List
from pydantic import BaseModel, Field


class InputTaskModel(BaseModel):
    """
    Модель входных данных для задачи склейки русел
    """

    tasks: List[Task] = Field(alias="tasks")








