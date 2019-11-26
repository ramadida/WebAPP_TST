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

@app.route('/film/popular')
def popular():
    try :
        movie = Movie()
        popular = movie.popular()

        data = []
        for p in popular:
            data.append({
                'id' : p.id,
                'title' : p.title,
                'overview' : p.overview,
                'poster_path' : p.poster_path
            })

        return jsonify(data)

    except Exception as e :
        abort(404)

@app.route('/film/detailfilm/<id>')
def detailfilm(id):
    try :
        movie = Movie()
        m = movie.details(id)

        data = []
        data.append({
            'title' : m.title,
            'overview' : m.overview,
            'popularity' : m.popularity
        })

        return jsonify(data)

    except Exception as e :
        abort(404)

@app.route('/film/moviebytitle/<title>')
def moviebytitle(title):
    try :
        movie = Movie()
        search = movie.search(title)

        data = []
        for res in search:
            data.append({
                'id' : res.id,
                'title' : res.title,
                'overview' : res.overview,
                'poster_path' : res.poster_path,
                'vote_avarage' : res.vote_average
            })

        return jsonify(data)

    except Exception as e :
        abort(404)

@app.route('/film/findmovbyid/<id>')
def findmovbyid(id):
    try :
        movie = Movie()
        similar = movie.similar(id)

        data = []
        for result in similar:
            data.append({
            'title' : result.title,
            'overview' : result.overview
        })

        return jsonify(data)

    except Exception as e :
        abort(404)

if __name__ == '__main__':
    #create_table()
    app.run(debug=True)