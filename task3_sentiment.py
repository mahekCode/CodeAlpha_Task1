from textblob import TextBlob
import pandas as pd

# Load dataset
df = pd.read_csv("task1_dataset1.csv")

# Function to get sentiment
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment function
df["Sentiment"] = df["Quote"].apply(get_sentiment)

# Show result
print(df)

# Save result to new CSV
df.to_csv("sentiment_result.csv", index=False)

print("Sentiment analysis completed and saved to sentiment_result.csv")