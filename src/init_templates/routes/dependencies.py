from fastapi import Depends
from ..utils.database import DatabaseConnection
from typing import Any


# def get_db() -> Any:
#   return DatabaseConnection.get_connection() # TODO: Add your database class' call to get_connection


"""
    REPOSITORY DEPENDENCIES
"""

# EXAMPLE
# def get_some_repo(db: Any = Depends(get_db)) -> SomeRepository:
#     return SomeRepository(db)


"""
    SERVICE DEPENDENCIES
"""

# EXAMPLE
# def get_some_service(some_repo: SomeRepository = Depends(get_some_repository)) -> SomeService:
#     return SomeService(some_repo)
