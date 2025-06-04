from typing import Annotated, List

from fastapi import APIRouter, Depends
from fastapi import status as status_code
from shared.settings import api_prefix_config

from .deps import get_question_service
from .schemas import QuestionIn, QuestionOut
from .service import QuestionService

router = APIRouter(prefix=api_prefix_config.v1.questions, tags=["Questions"])


@router.get("/create-table", status_code=status_code.HTTP_201_CREATED)
async def create_question_table(
    service: Annotated[QuestionService, Depends(get_question_service)],
):
    await service.create_question_table()


@router.get("/insert-mock", status_code=status_code.HTTP_200_OK)
async def insert_mock_questions(
    service: Annotated[QuestionService, Depends(get_question_service)],
):
    await service.insert_mock_questions()


@router.post("/find-most-similar", response_model=QuestionOut)
async def find_most_similar_question(
    data: QuestionIn,
    service: Annotated[QuestionService, Depends(get_question_service)],
):
    return await service.get_most_similar_question(question_text=data.question)


@router.post("/find-limited-similar", response_model=List[QuestionOut])
async def find_top_limited_similar(
    data: QuestionIn,
    service: Annotated[QuestionService, Depends(get_question_service)],
):
    return await service.get_top_limited_similar_questions(question_text=data.question)
