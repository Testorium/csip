from typing import TYPE_CHECKING, List

from fastapi import HTTPException
from fastapi import status as status_code
from shared.utils.logging import logger

from .mock_data import mock_questions
from .queries import (
    CREATE_QUESTIONS_TABLE_QUERY,
    FIND_MOST_SIMILAR_QUESTION_QUERY,
    FIND_TOP_LIMITED_SIMILAR_QUESTIONS_QUERY,
    INSERT_QUESTION_QUERY,
)
from .schemas import QuestionOut
from .tokenizer import Tokenizer

if TYPE_CHECKING:
    from asyncpg import Pool


class QuestionService:
    def __init__(self, db_pool: "Pool"):
        self.db_pool = db_pool
        self.tokenizer = Tokenizer()

    async def create_question_table(self) -> None:
        try:
            async with self.db_pool.acquire() as conn:
                await conn.execute(CREATE_QUESTIONS_TABLE_QUERY)

        except Exception as e:
            logger.exception("Failed to create question table.")
            raise HTTPException(
                status_code=status_code.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to create question table.",
            )

    async def insert_mock_questions(self) -> None:
        for question in mock_questions:
            self.insert_question(
                question_text=question.get("question"),
                answer=question.get(
                    "answer",
                ),
            )

    async def insert_question(
        self,
        question_text: str,
        answer: str,
    ) -> None:
        vector_literal = self._get_vector_literal(question_text)
        try:
            async with self.db_pool.acquire() as conn:
                await conn.execute(
                    INSERT_QUESTION_QUERY,
                    question_text,
                    answer,
                    vector_literal,
                )

        except Exception as e:
            logger.exception("Failed to insert question.")
            raise HTTPException(
                status_code=status_code.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to insert question.",
            )

    async def get_most_similar_question(self, question_text: str) -> QuestionOut:
        vector_literal = self._get_vector_literal(question_text)

        try:
            async with self.db_pool.acquire() as conn:
                row = await conn.fetchrow(
                    FIND_MOST_SIMILAR_QUESTION_QUERY, vector_literal
                )

        except Exception as e:
            logger.exception("Failed to retrieve most similar question.")
            raise HTTPException(
                status_code=status_code.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Similarity search failed.",
            )

        if not row:
            raise HTTPException(
                status_code=status_code.HTTP_404_NOT_FOUND,
                detail="No similar question found.",
            )
        return QuestionOut(**dict(row))

    async def get_top_limited_similar_questions(
        self,
        question_text: str,
        limit: int = 5,
    ) -> List[QuestionOut]:
        vector_literal = self._get_vector_literal(question_text)

        try:
            async with self.db_pool.acquire() as conn:
                rows = await conn.fetch(
                    FIND_TOP_LIMITED_SIMILAR_QUESTIONS_QUERY,
                    vector_literal,
                    limit,
                )

        except Exception as e:
            logger.exception("Failed to retrieve similar questions.")
            raise HTTPException(
                status_code=status_code.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Similarity search failed.",
            )

        return [QuestionOut(**dict(row)) for row in rows]

    def _get_vector_literal(self, question: str) -> str:
        embedding = self.tokenizer.get_token(question)
        return self.tokenizer.vector_to_pg_literal(embedding)
