import hashlib
import psycopg2
import psycopg2.extras
from flask import session
from app.app import app
from db.database_config import Database
from db.connection import start_connection, close_connection
from app.resources.Common.UsersCommon import UsersCommon


password = UsersCommon.to_hash('123Wertyq')
users = [
    {
        'email': "test@mail.ru",
        'login': 'test',
        'password': password
    }
]

videos = [
    {
        "title": "12.mov",
        "quality": "480p",
        "genres": ["Comedy"],
        "year": 2018,
        "rating": 8,
        "summary": "asdjaskdjaksdjasd"
    }
]


def create_user(user):
    sql = """INSERT INTO   users (email, login, password)
                     VALUES (%s, %s, %s)
                    ;"""
    record = (user['email'], user['login'], user['password'])
    cursor.execute(sql, record)
    connection.commit()


def create_video(video):
    sql = """INSERT INTO   videos (torrent_id, title, quality, genres, year, rating, summary)
                     VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ;"""
    record = (torrent_id, video['title'], video['quality'], video['genres'],
              video['year'], video['rating'], video['summary'])
    cursor.execute(sql, record)
    connection.commit()


connection, cursor = start_connection()
try:
    for user in users:
        create_user(user)
    torrent_id = 1
    for video in videos:
        create_video(video)
        torrent_id += 1

except Exception as e:
    print(e)
finally:
    close_connection(connection, cursor)