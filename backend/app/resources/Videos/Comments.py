from app.resources.Common.Base import Base
from flask import request, session
from flask_jwt_extended import jwt_required


class Comments(Base):

    # @jwt_required
    def get(self):
        video_id = request.args.get("video_id")
        sql = """
                SELECT  *
                FROM comments
                WHERE video_id = %s
            ;"""
        record = (video_id, )
        videos = self.base_get_limited_all(sql, record)
        return videos

    # @jwt_required
    def post(self):
        video_id = request.json['video_id']
        author = request.json['author']
        message = request.json['message']
        creation_date = request.json['creation_date']
        record = (video_id, author, message, creation_date)
        sql = '''INSERT INTO comments (video_id, author, message, creation_date)
                 VALUES (%s, %s, %s, %s);'''
        res = self.base_write(sql, record)
        return res
