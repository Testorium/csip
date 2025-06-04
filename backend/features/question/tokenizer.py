import torch
from sentence_transformers import SentenceTransformer


class Tokenizer:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def get_token(self, text: str) -> list[float]:
        embedding = self.model.encode(
            [text],
            convert_to_numpy=True,
            normalize_embeddings=True,
            show_progress_bar=False,
            device="cuda" if torch.cuda.is_available() else "cpu",
        )
        return embedding[0].tolist()

    @staticmethod
    def vector_to_pg_literal(vector: list[float]) -> str:
        return "[" + ", ".join(f"{x}" for x in vector) + "]"
