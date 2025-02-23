# NEON ONLINE DB CONNECTION

import requests
import psycopg2
import random
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


def get_connection():
    """Establish and return a connection to the Neon database."""
    try:
        connection = psycopg2.connect(DATABASE_URL)
        return connection
    except Exception as e:
        print("Error connecting to the database:", e)
        return None


def create_table():
    """Creates the vocabulary_noun table if it does not already exist."""
    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vocabulary_noun (
                id SERIAL PRIMARY KEY,
                difficulty_level INT CHECK (difficulty_level BETWEEN 1 AND 5),
                category VARCHAR(100),
                english_word VARCHAR(255) NOT NULL,
                portuguese_word VARCHAR(255) NOT NULL,
                phonetic VARCHAR(255),
                association TEXT
            );
        ''')
        conn.commit()
        cursor.close()
        conn.close()
        print("Table checked/created successfully.")
    except Exception as e:
        print("Error creating table:", e)


# Run this only once when setting up the database
if __name__ == "__main__":
    create_table()
