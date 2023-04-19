import psycopg2
from psycopg2 import pool
import os

threaded_postgreSQL_pool = psycopg2.pool.ThreadedConnectionPool(
    5,
    20,
    user=os.getenv("DB_USER","jayeshdalal"),
    password=os.getenv("DB_PASSWORD",""),
    host=os.getenv("DB_HOST","127.0.0.1"),
    port="5432",
    database=os.getenv("DB_NAME","assignmnet"),
)


def get_connections():
    if threaded_postgreSQL_pool:
        ps_connection = threaded_postgreSQL_pool.getconn()
        return ps_connection


def release_connection(ps_connection):
    threaded_postgreSQL_pool.putconn(ps_connection)
