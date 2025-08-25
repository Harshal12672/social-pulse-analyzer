from fastapi import FastAPI, Query
import sqlite3
import pandas as pd

app = FastAPI()

def get_connection():
    return sqlite3.connect("social_media.db")

@app.get("/")
def home():
    return {"message": "🚀 Social Pulse Analyzer API is running"}

@app.get("/dashboard-summary")
def dashboard_summary():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM social_posts", conn)
    conn.close()
    summary = {
        "total_posts": len(df),
        "avg_engagement_rate": round(df['engagement_rate'].mean(), 2),
        "date_range": f"{df['timestamp'].min()} to {df['timestamp'].max()}"
    }
    return summary

@app.get("/top-posts")
def top_posts(limit: int = 10):
    conn = get_connection()
    query = f"""
    SELECT post_id, platform, post_text, engagement_rate
    FROM social_posts
    ORDER BY engagement_rate DESC
    LIMIT {limit}
    """
    result = pd.read_sql(query, conn).to_dict(orient="records")
    conn.close()
    return result

@app.get("/engagement-by-platform")
def engagement_platform():
    conn = get_connection()
    query = """
    SELECT platform, ROUND(AVG(engagement_rate), 2) AS avg_engagement
    FROM social_posts
    GROUP BY platform
    """
    result = pd.read_sql(query, conn).to_dict(orient="records")
    conn.close()
    return result

@app.get("/engagement-by-time")
def engagement_time(time_unit: str = Query("day_of_week")):
    valid_units = ["hour_of_day", "day_of_week", "month"]
    if time_unit not in valid_units:
        return {"error": f"Invalid time_unit. Choose from {valid_units}"}
    
    conn = get_connection()
    query = f"""
    SELECT {time_unit}, ROUND(AVG(engagement_rate), 2) AS avg_engagement
    FROM social_posts
    GROUP BY {time_unit}
    ORDER BY avg_engagement DESC
    """
    result = pd.read_sql(query, conn).to_dict(orient="records")
    conn.close()
    return result
