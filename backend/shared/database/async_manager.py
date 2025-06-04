from typing import Optional

import asyncpg
from loguru import logger

from shared.settings import db_config

from .exc import ConnectionPoolNotInitialized, PoolClosureError, PoolInitializationError


class AsyncPostgresPoolManager:
    def __init__(
        self,
        dsn: str,
        min_pool_size: int = 1,
        max_pool_size: int = 10,
    ) -> None:
        self.dns = dsn
        self.min_pool_size = min_pool_size
        self.max_pool_size = max_pool_size
        self.db_pool: Optional[asyncpg.Pool] = None

    async def init_pool(self) -> None:
        try:
            self.db_pool = await asyncpg.create_pool(
                dsn=self.dns,
                min_size=self.min_pool_size,
                max_size=self.max_pool_size,
            )

        except Exception as e:
            logger.exception("Error initializing connection pool.")
            raise PoolInitializationError(str(e)) from e

    async def get_pool(self) -> asyncpg.Pool:

        if self.db_pool is None:
            logger.error("Connection pool is not initialized.")
            raise ConnectionPoolNotInitialized("Connection pool is not initialized.")

        try:
            return self.db_pool

        except Exception as e:
            logger.exception("Failed to return connection pool.")
            ConnectionPoolNotInitialized("Connection pool is not initialized.")

    async def close_pool(self) -> None:
        if self.db_pool is None:
            logger.error("Connection pool is not initialized.")
            raise ConnectionPoolNotInitialized("Connection pool is not initialized.")

        try:
            await self.db_pool.close()
        except Exception as e:
            logger.exception("Error while closing connection pool.")
            raise PoolClosureError(str(e)) from e


db_manager = AsyncPostgresPoolManager(
    dsn=db_config.dns,
    max_pool_size=db_config.max_pool_size,
    min_pool_size=db_config.min_pool_size,
)
