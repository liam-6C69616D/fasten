from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional
from ..utils.database_connection import DatabaseConnection

T = TypeVar('T')
CreateSchemaT = TypeVar('CreateSchemaT')
UpdateSchemaT = TypeVar('UpdateSchemaT')


class BaseRepository(ABC, Generic[T, CreateSchemaT, UpdateSchemaT]):
    """Abstract base repository. Uses injected DBConnection."""

    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection

    @abstractmethod
    def create(self, schema: CreateSchemaT) -> T:
        pass

    @abstractmethod
    def get_by_id(self, id: int | str) -> Optional[T]:
        pass

    @abstractmethod
    def get_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        pass

    @abstractmethod
    def update(self, id: int | str, schema: UpdateSchemaT) -> Optional[T]:
        pass

    @abstractmethod
    def delete(self, id: int | str) -> bool:
        pass
