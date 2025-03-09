"""
Author: Shravani Dadasaheb Aute
Date: March 7, 2025
Project: Sentiment Analysis using Flask & ML Model
Description: This Flask application loads a trained sentiment analysis model and predicts the sentiment of user-inputted text.


"""


from flask import Flask, request, render_template
import joblib
import os

app = Flask(__name__)

# Define model path
model_path = os.path.join(os.path.dirname(__file__), "sentiment_model.pkl")

# Load the trained model
if os.path.exists(model_path):
    model = joblib.load(model_path)
    print("✅ Model Loaded Successfully!")
else:
    raise FileNotFoundError(f"❌ Model not found at {model_path}")

@app.route("/", methods=["GET", "POST"])

  
    #Handles the main page. Accepts user input, predicts sentiment, and displays the result.
   
def index():
    sentiment = None
    if request.method == "POST":
        review = request.form.get("review")  # Use .get() to avoid KeyError
        if review:  # Ensure review is not empty
            prediction = model.predict([review])
            sentiment = "Positive" if prediction[0] == 1 else "Negative"
    return render_template("index.html", sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)
