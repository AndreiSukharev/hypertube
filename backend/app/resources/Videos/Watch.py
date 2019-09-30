from app.resources.Common.Base import Base
from app.resources.TorrentManager.TorrentManager import TorrentManager
from flask import request, session, send_file
from flask_jwt_extended import jwt_required
import requests


class Watch(Base):

    def get(self, torrent_id):
        movie = self.check_movies_exist_in_db(torrent_id)
        if movie:
            print(movie)
            return send_file('../videos_hub/' + movie['title'])
        # data = self.get_movie(torrent_id)
        # if not self.check_movies_exist_in_torrent(data):
        #     return {"msg": "error"}
        # path = self.download_torrent(data['data']['movie']['torrents'][0]['url'])
        return send_file('../videos_hub/12.mov')
        # path ='/usr/src/backend/torrents/debian-10.1.0-amd64-netinst.iso.torrent'
        # res = TorrentManager.manage(path)
        # return res

    @staticmethod
    def get_movie(torrent_id):
        url = "https://yts-am-torrent.p.rapidapi.com/movie_details.json"
        querystring = {"movie_id": torrent_id}
        headers = {
            'x-rapidapi-host': "yts-am-torrent.p.rapidapi.com",
            'x-rapidapi-key': "017fa83186msh61e30cfdc3ccdf1p1292c9jsn5a288faa0a35"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()

    def download_torrent(self, url):
        filename = url.split('/')[-1] + '.torrent'
        print(filename)
        path = '/usr/src/backend/torrents/' + filename
        r = requests.get(url=url, allow_redirects=True)
        with open(path, 'wb') as f:
            f.write(r.content)
        return path

    @staticmethod
    def check_movies_exist_in_torrent(data):
        if data['status'] == 'ok':
            return True
        return False

    def check_movies_exist_in_db(self, torrent_id):
        sql = """   SELECT title
                    FROM videos
                    WHERE torrent_id=%s;"""
        record = (torrent_id,)
        movie = self.base_get_one(sql, record)
        return movie


