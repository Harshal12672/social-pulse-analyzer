📊 Social Pulse Analyzer – Project Summary
🔎 Overview

Social Pulse Analyzer ek end-to-end data pipeline + analytics + visualization project hai jo social media engagement ko analyze karta hai.
Iska main goal hai:
👉 Content creators aur marketers ko batana kaunsa content sabse zyada engagement laata hai, aur kis platform/day par unka content best perform karta hai.

🏗️ Project Workflow
1. Data Ingestion

Fake / sample social media posts generate kiye gaye

Data save kiya gaya in CSV (raw_data.csv)

📂 File: data_ingestion.py

2. Data Cleaning & Feature Engineering

Missing values handle kiye

Naye features banaye (jaise post_text_length, hashtag_count, hour_of_day, day_of_week, month)

Clean data save kiya in cleaned_data.csv

📂 File: data_cleaner.py

3. Database Management

Clean data ko SQLite database (social_media.db) me insert kiya

Database future queries ke liye ready hai

📂 File: database_manager.py

4. Data Analysis

Engagement rate calculate kiya = (likes + comments + shares) / followers

Top 10 posts by engagement identify kiye

Average engagement by platform (Facebook, Twitter, Instagram) nikala

Average engagement by day of week nikala

📂 File: analyzer.py

5. REST API (Backend)

FastAPI ka use karke API banayi

Endpoints provide karte hain:

Top posts

Engagement by platform

Engagement by weekday

📂 File: main_api.py

Run using:

uvicorn main_api:app --reload

6. Interactive Dashboard (Frontend)

Streamlit ka use karke visualization banayi

User-friendly dashboard with:

Bar charts

Tables

Engagement trends
🛠️ Tech Stack

Programming: Python (Pandas, NumPy)

Database: SQLite

Backend API: FastAPI + Uvicorn

Frontend Dashboard: Streamlit

Deployment: Docker

🚀 Key Features

✅ Automated pipeline from raw data → cleaned data → database → analysis
✅ REST API for programmatic access
✅ Interactive Streamlit dashboard for visualization
✅ Cross-platform deployment via Docker

📈 Example Outputs

Top Posts by Engagement:
Shows best-performing posts.

Engagement by Platform:
Compare Facebook vs Twitter vs Instagram.

Engagement by Day:
Shows best day to post for higher engagement.

🎯 Use Cases

Marketing teams → find best posting time & content

Content creators → understand which posts perform better

Data science students → learn end-to-end project with ETL, API, dashboard, and Docker

✅ Final Deliverables

Python scripts (data_ingestion.py, data_cleaner.py, etc.)

SQLite database (social_media.db)

REST API (main_api.py)

Streamlit Dashboard (dashboard_ui.py)

📂 File: dashboard_ui.py

Run using:

streamlit run dashboard_ui.py
