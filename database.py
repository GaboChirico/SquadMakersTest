import os
import psycopg2


# Set up database connection
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="squad_makers",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])
    return conn

# Close database connection
def close_db_connection(conn):
    conn.close()

# Initialize database and table
def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS jokes;')
    cur.execute(
        "CREATE TABLE IF NOT EXISTS jokes (id serial PRIMARY KEY, joke text, date DEFAULT CURRENT_TIMESTAMP)")
    conn.commit()
    close_db_connection(conn)

# Get all jokes
def get_jokes(id=None):
    conn = get_db_connection()
    cur = conn.cursor()
    if id:
        cur.execute("SELECT * FROM jokes WHERE id = %s", (id))
    else:
        cur.execute("SELECT * FROM jokes")
    jokes = cur.fetchall()
    close_db_connection(conn)
    return jokes

# Insert a joke
def insert_joke(joke):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO jokes (joke) VALUES (%s)", (joke))
    conn.commit()
    close_db_connection(conn)

# Update a joke
def edit_joke(id, joke):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE jokes SET joke = %s WHERE id = %s", (joke, id))
    conn.commit()
    close_db_connection(conn)

# Delete a joke
def delete_joke(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM jokes WHERE id = %s", (id))
    conn.commit()
    close_db_connection(conn)
