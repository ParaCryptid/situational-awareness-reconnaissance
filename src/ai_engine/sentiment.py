
from transformers import pipeline

def analyze_sentiment(text):
    nlp = pipeline("sentiment-analysis")
    return nlp(text)
