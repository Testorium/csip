import os

from dotenv import load_dotenv

load_dotenv()


class GunicornConfig:
    host: str = "0.0.0.0"
    port: int = 8000
    timeout: int = 900
    workers: int = 1
    log_level: str = "info"


gunicorn_config = GunicornConfig()


class DatabaseConfig:
    driver: str = "postgresql"
    user: str = os.getenv("POSTGRES_USER")
    password: str = os.getenv("POSTGRES_PASSWORD")
    host: str = os.getenv("POSTGRES_HOST")
    port: int = os.getenv("POSTGRES_PORT")
    db_name: str = os.getenv("POSTGRES_DB")

    min_pool_size: int = int(os.getenv("DB_MIN_POOL_SIZE", 1))
    max_pool_size: int = int(os.getenv("DB_MAX_POOL_SIZE", 10))

    @property
    def dns(self) -> str:
        return f"{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"


db_config = DatabaseConfig()


class APIV1PrefixConfig:
    prefix: str = "/v1"
    questions: str = "/questions"


class APIPrefixConfig:
    prefix: str = "/api"
    v1: APIV1PrefixConfig = APIV1PrefixConfig()


api_prefix_config = APIPrefixConfig()
