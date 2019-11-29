import tweepy
from flask import Flask, render_template, request, jsonify
import requests
import json

consumer_key = "vun19WFwsJNMOG8zTcWIgHaRP"
consumer_secret = "6vP95kbUUdHGqCYtY4DXfNyJTa2wFdTf598jKZazKqiKOjSJNu"
access_token = "83359542-CbOtYl25zVKKlVaAEhPvsa3oHq9f73JGNanTC5nit"
access_secret = "sNZhq5WpXTAqo0aecYruGYcXnx1W5RISqXhGGycklMFxE"

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
    data = requests.get('http://localhost:5001/movie/now_playing').json()
    return render_template('nowplaying.html', nps=data)

@app.route('/movie/upcoming')
def upcoming():
    dataa = requests.get('http://localhost:5001/movie/upcoming').json()
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
