''' This function initiates the Emotion Detection application
    using Flask and deploying on localhost:5000
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def send_emotion_text():
    ''' This code receives text from user and runs 
        emotion_detector() function. The output returns
        the desired emotion score and the dominant emotion
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # pylint: disable=consider-using-f-string
    return "For the given statement, the system response is 'anger': {}, 'disgust': {},"\
    "'fear': {}, 'joy': {}, and 'sadness': {}. The dominant emotion is {}".format(anger, 
    disgust, fear, joy, sadness, dominant_emotion)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main
        application page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
