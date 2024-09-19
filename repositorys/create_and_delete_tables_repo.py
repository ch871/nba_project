import psycopg2
from psycopg2.extras import RealDictCursor
from config.sql_config import SQLALCHEMY_DATABASE_URI


def get_db_connection():
    return psycopg2.connect(SQLALCHEMY_DATABASE_URI, cursor_factory=RealDictCursor)


def drop_all_tables():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
        DROP TABLE "2024";
        DROP TABLE "2023";
        DROP TABLE "2022";
        )
        ''')
    connection.commit()
    cursor.close()
    connection.close()


def create_players_table(season):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {season} (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        team VARCHAR(100) NOT NULL,
        position VARCHAR(100) NOT NULL,
        points INTEGER NOT NULL,
        games INTEGER NOT NULL,
        shooting_2 INTEGER NOT NULL,
        shooting_3 INTEGER NOT NULL,
        minutes FLOAT NOT NULL,
        at_ratio FLOAT NOT NULL,
        ppg_ratio FLOAT NOT NULL,      
    )
    ''')
    connection.commit()
    cursor.close()
    connection.close()
