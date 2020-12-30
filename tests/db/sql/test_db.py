from unittest import TestCase, skip

import psycopg2


@skip
class RowLevelSecurityTest(TestCase):
    def setUp(self) -> None:
        conn = psycopg2.connect(dbname="testdb", user="postgres", password="postgres", port="5435")

        cur = conn.cursor()
        cur.execute("""DROP TABLE IF EXISTS song;""")
        cur.execute("""DROP ROLE IF EXISTS testrole""")
        cur.execute("""DROP ROLE IF EXISTS anon""")

        conn.commit()
        conn.close()

    def test_rls(self):
        conn = psycopg2.connect(dbname="testdb", user="postgres", password="postgres", port="5435")
        cur = conn.cursor()
        cur.execute("CREATE ROLE testrole")
        cur.execute("CREATE ROLE anon")
        cur.execute("""CREATE TABLE song (id SERIAL PRIMARY KEY , oid VARCHAR(255), name VARCHAR(255));""")
        cur.execute("""ALTER TABLE song ENABLE ROW LEVEL SECURITY;""")
        cur.execute("""CREATE POLICY rls_song ON song USING (oid = current_user);""")
        cur.execute("""GRANT select, insert ON song TO testrole;""")
        cur.execute("""GRANT select, insert ON song TO anon;""")

        cur.execute("INSERT INTO song (oid, name) VALUES ('testrole', 'Geronimos Cadillac')")
        conn.commit()
        conn.close()

        conn = psycopg2.connect(dbname="testdb", user="postgres", password="postgres", port="5435")
        cur = conn.cursor()
        cur.execute("SELECT * FROM song")
        res = cur.fetchall()
        print('superuser', res)

        cur.execute("SET ROLE testrole")
        cur.execute("SELECT * FROM song")
        res = cur.fetchall()
        print('testrole', res)

        cur.execute("SET ROLE anon")
        cur.execute("SELECT * FROM song")
        res = cur.fetchall()
        print('anon', res)
        conn.close()
