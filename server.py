from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def send_emotion_text():
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    anger = response['anger']

    return "For the given statement, the system response is 'anger': {}".format(anger)

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)