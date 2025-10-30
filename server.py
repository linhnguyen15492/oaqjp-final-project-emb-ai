"""This module provides functionality for dectect emotion of text provided."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
        route to receive text to analyze emotion
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get("textToAnalyze")

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the response is None, indicating an error or invalid input
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Return a formatted string with the sentiment label and score
    return f"For the given statement, the system response is \
                'anger': {response['anger']}, 'disgust': {response['disgust']}, \
                'fear': {response['fear']}, 'joy': {response['joy']} and \
                'sadness': {response['sadness']}. \
                The dominant emotion is {response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    """
        render main page of the web application
    """
    # This function initiates the rendering of the main application page over the Flask channel
    return render_template("index.html")

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
