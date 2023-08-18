import psycopg2
from config import host, user, password, db_name

def connect():
    connection = None
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )

        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT version();"
            )

            print(f"Server version: {cursor.fetchone()}")

        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT 
                    generate_series(
                        CURRENT_DATE,
                        CURRENT_DATE + INTERVAL '99 days',
                        (random() * 5 + 2) * INTERVAL '1 day'
                    )::DATE AS date_value;"""
            )

            print(f"Redy,  {cursor.fetchone()}")

    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")

if __name__ == '__main__':
    connect()