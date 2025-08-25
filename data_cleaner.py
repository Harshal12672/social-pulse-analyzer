import pandas as pd
import re

def clean_text(text):
    text = re.sub(r"http\S+", "", text)                     # remove URLs
    text = re.sub(r"[^a-zA-Z0-9\s#]", "", text)             # remove special characters
    text = re.sub(r"\s+", " ", text).strip().lower()        # lowercase and trim
    return text

def clean_data(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    df['likes'] = df['likes'].fillna(0)
    df['comments'] = df['comments'].fillna(0)
    df['shares'] = df['shares'].fillna(0)
    df['views'] = df['views'].replace(0, 1)  # avoid divide by zero

    # ➕ New Features
    df['engagement_rate'] = (df['likes'] + df['comments'] + df['shares']) / df['views']
    df['post_text'] = df['post_text'].apply(clean_text)
    df['post_text_length'] = df['post_text'].apply(len)
    df['hashtag_count'] = df['hashtags'].apply(lambda x: len(str(x).split(',')))
    df['hour_of_day'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.day_name()
    df['month'] = df['timestamp'].dt.month

    return df

# Run this script
if __name__ == "__main__":
    df = pd.read_csv("raw_data.csv")
    df_clean = clean_data(df)
    df_clean.to_csv("cleaned_data.csv", index=False)
    print("✅ Cleaned data saved to cleaned_data.csv")
