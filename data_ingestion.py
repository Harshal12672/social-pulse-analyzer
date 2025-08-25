import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_social_data(num_rows=1000):
    platforms = ['Twitter', 'Instagram', 'Facebook']
    sentiments = ['positive', 'neutral', 'negative']
    hashtags = ['#fun', '#news', '#trend', '#life']
    start_date = datetime(2024, 1, 1)

    data = []
    for i in range(num_rows):
        timestamp = start_date + timedelta(minutes=np.random.randint(0, 525600))
        platform = random.choice(platforms)
        post_text = f"Post number {i} is about something interesting!"
        likes = np.random.randint(0, 500)
        comments = np.random.randint(0, 100)
        shares = np.random.randint(0, 50)
        views = likes * np.random.uniform(1.5, 3.0)
        tags = random.sample(hashtags, k=random.randint(1, 2))
        sentiment = random.choice(sentiments)

        data.append({
            "post_id": i + 1,
            "timestamp": timestamp,
            "platform": platform,
            "post_text": post_text,
            "likes": likes,
            "comments": comments,
            "shares": shares,
            "views": int(views),
            "hashtags": ','.join(tags),
            "sentiment": sentiment
        })

    df = pd.DataFrame(data)
    return df

# Run and Save the data
if __name__ == "__main__":
    df = generate_social_data()
    df.to_csv("raw_data.csv", index=False)
    print("✅ Data saved to raw_data.csv")
