from typing import Final, Optional

from db.sql import queries


def authenticate(username: str, password: str) -> Optional[str]:
    """
    Returns an authentication token if username and password are correct.
    """
    sql: Final[str] = ""
    queries.get_row(sql, credentials=queries.get_db_master_credentials, )
