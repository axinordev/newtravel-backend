import time
import psycopg2

DB_NAME = "travel_db"
DB_USER = "postgres"
DB_PASSWORD = "Sumood@32"
DB_HOST = "db"
DB_PORT = "5432"

while True:
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.close()
        print("Database is ready!")
        break
    except:
        print("Waiting for database...")
        time.sleep(2)

