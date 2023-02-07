import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    sentiment = SentimentIntensityAnalyzer().polarity_scores(text)
    score = sentiment['compound']
    
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

nltk.download("vader_lexicon")

text = input("Enter a piece of text to analyze: ")
sentiment = analyze_sentiment(text)
print(f"Sentiment: {sentiment}")