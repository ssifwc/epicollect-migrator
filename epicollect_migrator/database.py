import psycopg2
from psycopg2.extras import execute_values


class Database:

    def __init__(self, connection, cursor):
        """
        :type connection: psycopg2.extensions.connection
        :type cursor: psycopg2.extensions.cursor
        """
        self._connection = connection
        self._cursor = cursor

    @classmethod
    def connect(cls, connection_uri):
        """"
        :type connection_uri: str
        :rtype: epicollect_migrator.database.Database
        """
        connection = psycopg2.connect(connection_uri)

        return cls(connection, connection.cursor())

    def add_field_observations(self, observation):
        sql = """
                INSERT INTO field_observations (
                    uuid,
                    coordinates,
                    flow_rate,
                    json_record)
                VALUES %s
                ON CONFLICT (uuid) DO UPDATE SET
                    uuid = excluded.uuid,
                    coordinates = excluded.coordinates,
                    flow_rate = excluded.flow_rate,
                    json_record = excluded.json_record;
                """
        execute_values(self._cursor, sql, observation)

    def close(self):
        self._connection.commit()
        self._cursor.close()
        self._connection.close()
