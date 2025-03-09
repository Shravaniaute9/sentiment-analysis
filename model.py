
"""
Sentiment Analysis Model Loader
Description: This script loads the trained ML model and provides a function to predict sentiment.
"""

import joblib
import os

# Define model path
model_path = os.path.join(os.path.dirname(__file__), "sentiment_model.pkl")

# Load model
def load_model():
    return joblib.load(model_path)

# Predict function
def predict_sentiment(text):
    model = load_model()
    prediction = model.predict([text])[0]
    return "Positive" if prediction == 1 else "Negative"