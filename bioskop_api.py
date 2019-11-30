import json
import sqlite3
from sqlite3 import Error

from flask import abort, Flask, jsonify, redirect, request, url_for

from tmdbv3api import TMDb, Movie


app = Flask(__name__)
tmdb = TMDb()
tmdb.api_key ='b566c7800e1ee8c398992a34065ede1f'

def response_api(data):
    """
    Fungsi untuk menampilkan data kedalam format Json.
    Key parameter data adalah dictionary dan mandatory.
    Berikut ini adalah contoh pengisian key parameter data:
    data = {
        'code': 200,
        'message': 'User berhasil ditemukan.',
        'data': [
            {
                'id': 1,
                'name': 'Kuda'
            }
        ]
    }
    """
    return (
        jsonify(**data),
        data['code']
    )

@app.errorhandler(400)
def bad_request(e):
    return response_api({
        'code': 400,
        'message': 'Ada kekeliruan input saat melakukan request.',
        'data': None
    })

@app.errorhandler(404)
def not_found(e):
    return response_api({
        'code': 404,
        'message': 'Film tidak berhasil ditemukan.',
        'data': None
    })

@app.errorhandler(405)
def method_not_allowed(e):
    return response_api({
        'code': 405,
        'message': 'Film tidak berhasil ditemukan.',
        'data': None
    })

@app.errorhandler(500)
def internal_server_error(e):
    return response_api({
        'code': 500,
        'message': 'Mohon maaf, ada gangguan pada server kami.',
        'data': None
    })

@app.route('/')
def root():
    return 'RESTful API Sederhana Menggunakan Flask'

@app.route('/movie/now_playing')
def now_playing():
    try :
        movie = Movie()
        now_playing = movie.now_playing()

        data = []
        for p in now_playing:
            data.append({
                'id' : p.id,
                'title' : p.title,
                'overview' : p.overview,
                'poster_path' : p.poster_path
            })

        return jsonify(data)

    except Exception as e :
        abort(404)

@app.route('/movie/upcoming')
def upcoming():
    try :
        movie = Movie()
        upcoming = movie.upcoming()

        data = []
        for p in upcoming:
            data.append({
                'id' : p.id,
                'title' : p.title,
                'overview' : p.overview,
                'poster_path' : p.poster_path
            })

        return jsonify(data)

    except Exception as e :
        abort(404)


if __name__ == '__main__':
    #create_table()
    app.run(port = 5001)