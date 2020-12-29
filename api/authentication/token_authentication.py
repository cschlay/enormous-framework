from typing import Final, Optional

from db.sql import queries


def authenticate(username, password) -> Optional[str]:
    """
    Returns an authentication token if username and password are correct otherwise None.
    """
    sql: Final[str] = ""
    queries.get_row(sql, credentials=queries.get_db_master_credentials, )

