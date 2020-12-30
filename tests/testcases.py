import os
import unittest

import psycopg2
from starlette.testclient import TestClient

from main import app


class APITestCase(unittest.TestCase):
    sql_files = []

    def tearDown(self) -> None:
        """Flushes the databases."""
        connection = psycopg2.connect(
            dbname="testdb",
            user="postgres",
            password="postgres",
            port=5435,
        )
        connection.set_session(autocommit=True)
        with connection.cursor() as cursor:
            cursor.execute("TRUNCATE app_user")     # All user data linked should get cleared.
        connection.close()

    @classmethod
    def tearDownClass(cls):
        """Delete the test database."""
        connection = psycopg2.connect(
            dbname="testdb",
            user="postgres",
            password="postgres",
            port=5435,
        )
        connection.set_session(autocommit=True)
        with connection.cursor() as cursor:
            cursor.execute("DROP SCHEMA public CASCADE")
            cursor.execute("CREATE SCHEMA public")
        connection.close()

    @classmethod
    def setUpClass(cls):
        """Set up the api client and the test database."""
        cls.client = TestClient(app)
        os.environ["DB_NAME"] = "testdb"
        os.environ["DB_USER"] = "postgres"
        os.environ["DB_PASSWORD"] = "postgres"
        os.environ["DB_HOST"] = "localhost"
        os.environ["DB_PORT"] = "5435"

        os.environ["REDIS_DB"] = "0"
        os.environ["REDIS_HOST"] = "localhost"
        os.environ["REDIS_PORT"] = "6379"

        connection = psycopg2.connect(
            dbname="testdb",
            user="postgres",
            password="postgres",
            port=5435,

        )
        connection.set_session(autocommit=True)
        # Create tables and insert data if in scripts.
        with connection.cursor() as cursor:
            for sql_file in ['_install'] + cls.sql_files:
                with open(f"resources/sql/{sql_file}.sql", "r") as file:
                    cursor.execute(file.read())
        connection.close()
