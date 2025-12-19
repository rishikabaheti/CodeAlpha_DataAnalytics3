import pandas as pd
from textblob import TextBlob

print("Sentiment Analysis Started")

# Sample data
data = {
    "Review": [
        "This movie is amazing",
        "I hated the acting",
        "The story was okay",
        "Excellent direction",
        "Waste of time"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Function to get sentiment
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df["Sentiment"] = df["Review"].apply(get_sentiment)

# Show result
print(df)
