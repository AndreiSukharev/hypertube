from app.resources.Common.Base import Base
from flask import request, session
from flask_jwt_extended import jwt_required
import requests


class Watch(Base):

    def get(self, movie_id):
        data = self.get_movie(movie_id)
        if not self.check_movies_exist(data):
            return {"msg": "error"}
        return data['data']['movie']['torrents']

    @staticmethod
    def get_movie(movie_id):
        url = "https://yts-am-torrent.p.rapidapi.com/movie_details.json"
        querystring = {"movie_id": "13723"}
        headers = {
            'x-rapidapi-host': "yts-am-torrent.p.rapidapi.com",
            'x-rapidapi-key': "017fa83186msh61e30cfdc3ccdf1p1292c9jsn5a288faa0a35"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        return response.json()

    @staticmethod
    def check_movies_exist(data):
        if data['status'] == 'ok':
            return True
        return False


    # detailed search video
    #
    # def post(self):
    #     genre = request.json['genre']
