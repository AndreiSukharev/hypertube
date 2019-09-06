from app.resources.Common.Base import Base
from flask import request, session
from flask_jwt_extended import jwt_required


class Search(Base):

    # search video by name
    def get(self, video_name):
        pass

    # detailed search video
    def post(self):
        genre = request.json['genre']
