import tweepy
from flask import Flask, render_template, request
import os
import requests


consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_secret = os.environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# API object
api = tweepy.API(auth)

app = Flask(__name__)


def filtersearch_tweets(search_word):
    result = []
    tweets = api.search(q=search_word, result_type="popular")
    for tweet in tweets:
        result.append({
            'Username': "@" + tweet.user.screen_name,
            'Tweets': tweet.text
        })
    return result


@app.route('/')
@app.route('/movie/now_playing')
def nowplaying():
    data = requests.get('https://bioskop-api.herokuapp.com/movie/now_playing').json()
    return render_template('nowplaying.html', nps=data)


@app.route('/movie/upcoming')
def upcoming():
    dataa = requests.get('https://bioskop-api.herokuapp.com/movie/upcoming').json()
    return render_template('comingsoon.html', ucs=dataa)


@app.route('/movie/getTweetsByFilter')
def movietweets():
    try:
        query = request.args.get('q')
        query.replace('%20', ' ')
        tweets = filtersearch_tweets(query)
        if tweets:
            return render_template('single_nowplaying.html', tws=tweets)
        else:
            return render_template('404.html')
    except Exception as e:
        raise e


if __name__ == '__main__':
    app.run(port=6969, debug=True)
