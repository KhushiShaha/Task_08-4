# Sentiment and Lexical Diversity Analysis
from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def lexical_diversity(text):
    words = text.split()
    return len(set(words)) / len(words) if words else 0

# Claude response
with open("../outputs/claude_confirmation_output.txt") as f:
    text = f.read()
    sentiment = analyze_sentiment(text)
    diversity = lexical_diversity(text)

with open("sentiment_lexical_results.txt", "w") as out:
    out.write(f"Claude - Sentiment Polarity: {sentiment:.2f}, Lexical Diversity: {diversity:.2f}\n")

# ChatGPT response
with open("../outputs/chatgpt_framing_output.txt") as f:
    text = f.read()
    sentiment = analyze_sentiment(text)
    diversity = lexical_diversity(text)

with open("sentiment_lexical_results.txt", "a") as out:
    out.write(f"ChatGPT - Sentiment Polarity: {sentiment:.2f}, Lexical Diversity: {diversity:.2f}\n")
