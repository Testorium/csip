from shared.schemas import BaseSchema


class QuestionIn(BaseSchema):
    question: str


class QuestionOut(BaseSchema):
    id: int
    question: str
    answer: str
    cosine_similarity: float | int
