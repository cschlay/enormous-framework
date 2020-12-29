from typing import Final

import argon2

from db.sql import queries


def create(username: str, password: str) -> dict:
    """
    Creates a new user if the username is not already used.

    :param username: The name to use
    :param password: Password in plain-text
    :return: created user as { id, username }
    """

    pid, username = queries.create_row(
        f"INSERT INTO app_user (username, password_hash) VALUES (%(username)s, %(password_hash)s) RETURNING pid, username",
        credentials=queries.get_db_master_credentials,
        username=username,
        password_hash=create_password(password)
    )
    return {
        "id": pid,
        "username": username,
    }


def create_password(plain_password: str) -> str:
    """Returns a password hash."""
    return argon2.PasswordHasher().hash(password=plain_password)
