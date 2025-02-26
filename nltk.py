from transformers import pipeline

def analyze_sentiment_hf(text):
    """
    Analyzes sentiment using Hugging Face Transformers.

    Args:
        text: The text to analyze.

    Returns:
        A dictionary containing the sentiment label and score.
    """
    try:
        sentiment_pipeline = pipeline("sentiment-analysis")
        result = sentiment_pipeline(text)[0] # pipeline returns a list of dictionaries
        return result
    except Exception as e:
        print(f"Error during sentiment analysis: {e}")
        return None

# Example Usage
review_text1 = "This movie was absolutely fantastic! I loved every minute."
sentiment1 = analyze_sentiment_hf(review_text1)
print(f"Review: '{review_text1}' - Sentiment: {sentiment1}")

review_text2 = "The movie was terrible. I wasted my time and money."
sentiment2 = analyze_sentiment_hf(review_text2)
print(f"Review: '{review_text2}' - Sentiment: {sentiment2}")

review_text3 = "The movie was okay, nothing special."
sentiment3 = analyze_sentiment_hf(review_text3)
print(f"Review: '{review_text3}' - Sentiment: {sentiment3}")

review_text4 = "I didn't like the movie but the acting was good."
sentiment4 = analyze_sentiment_hf(review_text4)
print(f"Review: '{review_text4}' - Sentiment: {sentiment4}")

review_text5 = "The plot was predictable, but the visuals were stunning."
sentiment5 = analyze_sentiment_hf(review_text5)
print(f"Review: '{review_text5}' - Sentiment: {sentiment5}")