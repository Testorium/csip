class DatabaseError(Exception):
    """Base class for all DB-related errors."""


class ConnectionPoolNotInitialized(DatabaseError):
    """Raised when the connection pool has not been initialized."""


class PoolInitializationError(DatabaseError):
    """Raised when initialization of the pool fails."""


class PoolClosureError(DatabaseError):
    """Raised when closing the pool fails."""
