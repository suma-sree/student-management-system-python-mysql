# database.py
# MySQL connection setup

import mysql.connector

# MySQL database credentials (edit accordingly)
HOST = "localhost"
USER = "root"
PASSWORD = "Suma@2004"  
DATABASE = "student_db"

def create_connection():
    """
    Create MySQL database connection.
    """
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

def create_table():
    """
    Create students table if not exists.
    """
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL,
            marks FLOAT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()
