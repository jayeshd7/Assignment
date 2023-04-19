import psycopg2
from psycopg2.extras import RealDictCursor

from app.db import db_connection
from app.db.models import UserDetails
import logging



def save(payload: UserDetails):
    try:
        ps_connection = db_connection.get_connections()
        if ps_connection:
            ps_cursor = ps_connection.cursor()
            postgres_insert_query = """ INSERT INTO users (userid,username,address,email) VALUES (%s,%s,%s,%s)"""
            record_to_insert = (
                payload.user_id,
                payload.user_name,
                payload.address,
                payload.email,
            )
            logging.info("record_to_insert", record_to_insert)
            ps_cursor.execute(postgres_insert_query, record_to_insert)
            ps_connection.commit()
            logging.info("record insert into users table successfully", payload)

            ps_cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error("Error while connecting to PostgreSQL", error)

    finally:
        logging.info("Put away a PostgreSQL connection")
        db_connection.release_connection(ps_connection)


def get(user_id: int):
    try:
        ps_connection = db_connection.get_connections()
        if ps_connection:
            ps_cursor = ps_connection.cursor(cursor_factory=RealDictCursor)
            sql_select_query = """select * from users where userid = %s"""
            ps_cursor.execute(sql_select_query, (user_id,))
            user_records = ps_cursor.fetchone()
            # logging.info("Displaying rows from users table", user_records)
            # print("user_records---", user_records)
            ps_cursor.close()
            if user_records is None:
                return None
            return UserDetails(
                user_id=user_id,
                user_name=user_records["username"],
                address=user_records["address"],
                email=user_records["email"],
            )

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error("Error while connecting to PostgreSQL", error)

    finally:
        logging.info("Put away a PostgreSQL connection")
        db_connection.release_connection(ps_connection)
