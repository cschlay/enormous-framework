import datetime
import secrets
from typing import Final, Optional

import argon2

from db.key_value import keyvalue_db
from db.sql import queries
from monitoring.audit_logger import AuditLogger


def authenticate(username: str, password: str) -> str:
    """
    Returns an authentication token if username and password are correct.

    :param username: to authenticate
    :param password: in plain text
    :return:
    """
    sql: Final[str] = "SELECT id, password_hash FROM app_user WHERE username=%(username)s"
    user = queries.get_row(sql, credentials=queries.get_db_master_credentials, username=username)
    # Test password hash, see https://pypi.org/project/argon2-cffi/
    hasher = argon2.PasswordHasher()
    if hasher.verify(user[1], password):
        return generate_token(user_id=user[0], username=username)

    # TODO: Implement BadRequest exception.


def generate_token(user_id: int, username: str) -> str:
    """
    Generates a new authorization token and saves it in memory.
    See: https://docs.python.org/3/library/secrets.html

    :param user_id: of a user to generate token for
    :param username: is used appended to token to ensure uniqueness
    :return: the generated token
    """

    AuditLogger().info(user_id=user_id, message=f"Generating authorization token for user: {user_id}.")

    # The documentation suggests 32 bytes
    recommended_byte_size: Final[int] = 32
    token: str = secrets.token_hex(recommended_byte_size)

    # TODO: Bake in username encoded in b64.
    # TODO: Check for collisions.

    keyvalue_db.set(f"user:{user_id}:auth_token:{token}", {
        "created_at": datetime.datetime.now()
    })

    return token
