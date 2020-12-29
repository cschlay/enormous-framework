import os

import psycopg2


def get_db_master_credentials():
    """
    Returns database master credentials as dict which can be passed to connection.
    Although it is called master you should use a restricted db user.
    """

    return {
        "dbname": os.environ["DB_NAME"],
        "user": os.environ["DB_USER"],
        "password": os.environ["DB_PASSWORD"],
        "host": os.environ["DB_HOST"],
        "port": os.environ["DB_PORT"]
    }


def get_row(sql: str, credentials: callable, **kwargs):
    """
    Find a row in database with given database credentials.

    :param sql: The sql query to run.
    :param credentials: callable that returns db credentials as list.
    :param kwargs: The arguments to pass to sql query.
    :return: the unprocessed row as retrieved
    """
    connection = psycopg2.connect(**credentials())
    with connection.cursor() as cursor:
        cursor.execute(sql, kwargs)
        data = cursor.fetchone()
    connection.close()
    return data


def create_row(sql: str, credentials: callable, **kwargs):
    """Create a single row to database table."""
    connection = psycopg2.connect(**credentials())
    with connection.cursor() as cursor:
        cursor.execute(sql, kwargs)
        data = cursor.fetchone()
    connection.commit()
    connection.close()
    return data
