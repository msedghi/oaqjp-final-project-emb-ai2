from flask import Flask, render_template, request

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detection():
    text_to_analyze = request.args.
    response = emotion_predictor(text_to_analyze)
    return ("For the given statement, the system response is "
                "'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. "
                "The dominant emotion is {}."
                .format(response['anger'], response['disgust'], response['fear'], 
                        response['joy'], response['sadness'], response['dominant_emotion'])

@app.rout("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
