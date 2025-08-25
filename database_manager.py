import sqlite3
import pandas as pd

def create_connection(db_name="social_media.db"):
    return sqlite3.connect(db_name)

def create_table(conn):
    query = """
    CREATE TABLE IF NOT EXISTS social_posts (
        post_id INTEGER PRIMARY KEY,
        timestamp TEXT,
        platform TEXT,
        post_text TEXT,
        likes INTEGER,
        comments INTEGER,
        shares INTEGER,
        views INTEGER,
        hashtags TEXT,
        sentiment TEXT,
        engagement_rate REAL,
        post_text_length INTEGER,
        hashtag_count INTEGER,
        hour_of_day INTEGER,
        day_of_week TEXT,
        month INTEGER
    )
    """
    conn.execute(query)
    conn.commit()

def insert_data(conn, df):
    df.to_sql("social_posts", conn, if_exists="replace", index=False)
    conn.commit()

# Run this script
if __name__ == "__main__":
    df = pd.read_csv("cleaned_data.csv")
    conn = create_connection()
    create_table(conn)
    insert_data(conn, df)
    conn.close()
    print("✅ Cleaned data inserted into social_media.db (SQLite)")
