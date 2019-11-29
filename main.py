from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def root():
    data = requests.get('http://localhost:5001/movie/now_playing').json()
    return render_template('nowplaying.html', nps=data)


@app.route('/getTweetsByFilter/<search_word>')
def movietweets(search_word):
    try:
        tweets = requests.get('http://localhost:5000/getTweetsByFilter/<search_word>')
        return render_template('single_nowplaying.html', Tweet=tweets.text, Username="@" + tweets.user.screen_name)
    except Exception as e:
        raise e


if __name__ == '__main__':
    app.run(port=5001, debug=True)
