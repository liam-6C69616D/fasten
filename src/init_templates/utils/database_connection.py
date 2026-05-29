from abc import ABC, abstractmethod
from typing import TypeVar, Any

T = TypeVar('T')


class DatabaseConnection(ABC):
    """
    Abstract base class for database connections.
    Users should extend this class and implement the abstract methods
    for their specific database system (MongoDB, PostgreSQL, SQLite, etc.).
    """

    @classmethod
    @abstractmethod
    def connect(cls, **kwargs) -> None:
        """
        Establish a connection to the database.

        Args:
            **kwargs: Database-specific connection parameters
                     (e.g., uri, host, port, username, password, database_name)
        """
        pass

    @classmethod
    @abstractmethod
    def disconnect(cls) -> None:
        """Close the database connection."""
        pass

    @classmethod
    @abstractmethod
    def get_connection(cls) -> Any:
        """
        Return the database connection object.

        Returns:
            The connection object (e.g., MongoClient, psycopg2 connection, etc.)

        Raises:
            RuntimeError: If the database is not connected
        """
        pass
