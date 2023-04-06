from flask import Flask, render_template, request
from model import SentimentClassifierBert

app = Flask(__name__)
classifier = SentimentClassifierBert()
toggle = False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        sentiment = classifier.classify(text)
        return render_template('index.html', sentiment=sentiment)
    return render_template('index.html', sentiment=None)

if __name__ == '__main__':
    app.run()

