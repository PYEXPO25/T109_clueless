from textblob import TextBlob

def analyze_sentiment(review_text):
    analysis = TextBlob(review_text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"
