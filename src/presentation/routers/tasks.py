from dataclasses import dataclass
from typing import Annotated, final

from fastapi import Body

from src.presentation.dtos.models import (
    AppointmentExecutorTaskData,
    Comment,
    CommentsTaskData,
    CreateTaskData,
    EditTaskData,
    Error,
    Task,
    UpdateDeadlineData,
    UpdateStatusData,
)
from src.presentation.routers.base import BaseRouter


@final
@dataclass(slots=True, frozen=True, kw_only=True)
class TasksRouter(BaseRouter):
    """Обработчик API запросов по задачам."""

    async def get(self, task_id: int) -> Task | Error:  # type: ignore[empty-body]
        """Получение задачи по ID."""

    async def delete(self, task_id: int) -> Error:  # type: ignore[empty-body]
        """Удаление задачи по ID."""

    async def edit(  # type: ignore[empty-body]
        self,
        task_id: int,
        task_data: Annotated[EditTaskData, Body()],
    ) -> Task | Error:
        """Редактирование данных по задаче по ID."""

    async def create(  # type: ignore[empty-body]
        self,
        task_data: Annotated[CreateTaskData, Body()],
    ) -> Task | Error:
        """Создание новой задачи."""

    async def assign_executor(  # type: ignore[empty-body]
        self,
        task_id: int,
        task_data: Annotated[AppointmentExecutorTaskData, Body()],
    ) -> Task | Error:
        """Назначение исполнителя задачи."""

    async def update_status(  # type: ignore[empty-body]
        self,
        task_id: int,
        status_data: Annotated[UpdateStatusData, Body()],
    ) -> Task | Error:
        """Обновление статуса задачи."""

    async def update_deadline(  # type: ignore[empty-body]
        self,
        task_id: int,
        deadline_data: Annotated[UpdateDeadlineData, Body()],
    ) -> Task | Error:
        """Обновление срока выполнения задачи."""

    async def add_comments(  # type: ignore[empty-body]
        self,
        task_id: int,
        comment_data: Annotated[CommentsTaskData, Body()],
    ) -> Comment | Error:
        """Добавление комментариев в задачу."""

    async def get_comments(  # type: ignore[empty-body]
        self,
        task_id: int,
        comment_data: Annotated[CommentsTaskData, Body()],
    ) -> Comment | Error:
        """Получение комментариев из задачи."""
