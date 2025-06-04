CREATE_QUESTIONS_TABLE_QUERY = """
    CREATE EXTENSION IF NOT EXISTS vector;

    CREATE TABLE IF NOT EXISTS questions (
        id SERIAL PRIMARY KEY,
        question TEXT NOT NULL,
        answer TEXT NOT NULL,
        question_embedding vector(384)
    );
"""

INSERT_QUESTION_QUERY = """
    INSERT INTO questions (
        question, 
        answer, 
        question_embedding
    ) VALUES (
        $1, $2, $3
    );
"""

FIND_MOST_SIMILAR_QUESTION_QUERY = """
    SELECT 
        id, 
        question, 
        answer, 
        1 - (question_embedding <=> $1) AS similarity_score
    FROM questions
    ORDER BY similarity_score DESC
    LIMIT 1;
"""

FIND_TOP_LIMITED_SIMILAR_QUESTIONS_QUERY = """
    SELECT 
        id, 
        question, 
        answer, 
        1 - (question_embedding <=> $1) AS similarity_score
    FROM questions
    ORDER BY similarity_score DESC
    LIMIT $2;
"""
