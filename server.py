"""Server code for emotion detector"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=["GET"])
def emotion_detect_route():
    """Endpoint to analyze text and return detected emotions."""
    text_to_analyse = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyse)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 400

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response


@app.route('/')
def render_index_page():
    """Render the homepage with input form."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
