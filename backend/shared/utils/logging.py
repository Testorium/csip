from loguru import logger

logger.add(
    "logs/app.log",
    format="{time} {level} {message}",
    level="INFO",
    enqueue=True,
)
