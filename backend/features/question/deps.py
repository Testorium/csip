from typing import TYPE_CHECKING, Annotated

from fastapi import Depends
from shared.database.async_manager import db_manager

from .service import QuestionService

if TYPE_CHECKING:
    from asyncpg import Pool


async def get_question_service(
    db_pool: Annotated["Pool", Depends(db_manager.get_pool)],
) -> QuestionService:
    return QuestionService(db_pool)
