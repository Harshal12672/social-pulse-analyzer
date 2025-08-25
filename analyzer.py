import sqlite3
import pandas as pd

def connect_db(db_name="social_media.db"):
    return sqlite3.connect(db_name)

# 📌 1. Top N Posts by Engagement Rate
def get_top_posts(conn, limit=10):
    query = f"""
    SELECT post_id, platform, post_text, engagement_rate
    FROM social_posts
    ORDER BY engagement_rate DESC
    LIMIT {limit};
    """
    return pd.read_sql(query, conn)

# 📌 2. Average Engagement by Platform
def engagement_by_platform(conn):
    query = """
    SELECT platform, AVG(engagement_rate) AS avg_engagement
    FROM social_posts
    GROUP BY platform;
    """
    return pd.read_sql(query, conn)

# 📌 3. Average Engagement by Day of Week
def engagement_by_day(conn):
    query = """
    SELECT day_of_week, AVG(engagement_rate) AS avg_engagement
    FROM social_posts
    GROUP BY day_of_week
    ORDER BY avg_engagement DESC;
    """
    return pd.read_sql(query, conn)

# 📌 Run & Test All
if __name__ == "__main__":
    conn = connect_db()

    print("\n🔝 Top 10 Posts by Engagement:\n")
    print(get_top_posts(conn))

    print("\n📊 Engagement by Platform:\n")
    print(engagement_by_platform(conn))

    print("\n📅 Engagement by Day of Week:\n")
    print(engagement_by_day(conn))

    conn.close()
