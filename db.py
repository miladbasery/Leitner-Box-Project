
import psycopg2
from psycopg2 import sql
import sys
import config

def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=config.DB_NAME,
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            port=config.DB_PORT
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        sys.exit(1)

def setup_database():

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            port=config.DB_PORT
        )
        conn.autocommit = True
        cur = conn.cursor()
        

        cur.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{config.DB_NAME}'")
        exists = cur.fetchone()
        if not exists:
            cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(config.DB_NAME)))
            print(f"Database '{config.DB_NAME}' created successfully.")
        
        cur.close()
        conn.close()
        

        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(100) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS cards (
                id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(id),
                question TEXT NOT NULL,
                answer TEXT NOT NULL,
                slot INTEGER DEFAULT 1,
                last_review_date DATE DEFAULT CURRENT_DATE
            )
        """)
        
        conn.commit()
        cur.close()
        conn.close()
        
    except Exception as e:
        print(f"Setup Error: {e}")