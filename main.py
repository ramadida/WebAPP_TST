from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def root():
	data = requests.get('http://localhost:5001/movie/now_playing').json()
	return render_template('nowplaying.html', nps = data)

if __name__ == '__main__':
	#app.run(threaded = True, port = 5000)
    app.run()
