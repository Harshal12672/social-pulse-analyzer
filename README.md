📊 Social Pulse Analyzer – Project Summary
Social Pulse Analyzer is an end-to-end data pipeline + analytics + visualization project designed to analyze social media engagement.
The main goal is:
👉 To help content creators and marketers identify which content drives the most engagement, and on which platform/day their posts perform best.

🏗️ Project Workflow
1. Data Ingestion

Generated fake/sample social media posts

Saved raw data in CSV (raw_data.csv)
📂 File: data_ingestion.py

2. Data Cleaning & Feature Engineering

Handled missing values

Engineered new features (post_text_length, hashtag_count, hour_of_day, day_of_week, month)

Saved cleaned dataset in cleaned_data.csv
📂 File: data_cleaner.py

3. Database Management

Inserted cleaned data into SQLite database (social_media.db)

Prepared database for future queries and analytics
📂 File: database_manager.py

4. Data Analysis

Calculated engagement rate = (likes + comments + shares) / followers

Identified Top 10 posts by engagement

Calculated average engagement by platform (Facebook, Twitter, Instagram)

Calculated average engagement by day of week
📂 File: analyzer.py

5. REST API (Backend)

Built using FastAPI

Provides endpoints for:

Top posts

Engagement by platform

Engagement by weekday
📂 File: main_api.py

Run with:

uvicorn main_api:app --reload

6. Interactive Dashboard (Frontend)

Developed using Streamlit

User-friendly dashboard includes:

Bar charts

Tables

Engagement trends visualization
📂 File: dashboard_ui.py

Run with:

streamlit run dashboard_ui.py
🛠️ Tech Stack

Programming: Python (Pandas, NumPy)

Database: SQLite

Backend API: FastAPI + Uvicorn

Frontend Dashboard: Streamlit

Deployment: Docker

🚀 Key Features

✅ Automated pipeline from raw data → cleaned data → database → analysis
✅ REST API for programmatic data access
✅ Interactive Streamlit dashboard for visualization
✅ Cross-platform deployment via Docker
