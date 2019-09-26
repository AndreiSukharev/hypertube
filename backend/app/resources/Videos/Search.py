from app.resources.Common.Base import Base
from flask import request, session
from flask_jwt_extended import jwt_required
import requests


class Search(Base):

    # search video by name
    def get(self):
        data = self.parse_params()
        res = self.check_movies_exist(data)
        return res

    @staticmethod
    def parse_params():
        title = request.args.get('title')
        genre = request.args.get('genre')
        minimum_rating = request.args.get('minimum_rating')
        url = "https://yts-am-torrent.p.rapidapi.com/list_movies.json"
        querystring = {"query_term": title, "limit": "10", "genre": genre, "minimum_rating": minimum_rating}
        headers = {
            'x-rapidapi-host': "yts-am-torrent.p.rapidapi.com",
            'x-rapidapi-key': "017fa83186msh61e30cfdc3ccdf1p1292c9jsn5a288faa0a35"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()

    @staticmethod
    def check_movies_exist(data):
        print(data['data'])
        if data['status'] != 'ok':
            return {"msg": "error"}
        if data['data'].get('movies'):
            return {"msg": "ok", "movies": data['data']['movies']}
        return {"msg": "no movies found"}


    # detailed search video
    #
    # def post(self):
    #     genre = request.json['genre']
