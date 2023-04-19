import psycopg2
from psycopg2 import pool

threaded_postgreSQL_pool = psycopg2.pool.ThreadedConnectionPool(
    5,
    20,
    user="jayeshdalal",
    password="",
    host="127.0.0.1",
    port="5432",
    database="assignmnet",
)


def get_connections():
    if threaded_postgreSQL_pool:
        ps_connection = threaded_postgreSQL_pool.getconn()
        return ps_connection


def release_connection(ps_connection):
    threaded_postgreSQL_pool.putconn(ps_connection)
