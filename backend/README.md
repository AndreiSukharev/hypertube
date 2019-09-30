# RESTful API Hypertube

#### Note
All data should be sent to server in JSON file.

Schemas are in backend/db/models.py

## Endpoints

### Sign Up
```
POST     /api/signup
```

These keys are required to sign up a user:
```
email, login, password
```
Example for POST:
```
{
    "email": "test@user.ru",
    "login": "test1",
    "password": "wertyq123"
}
 ```
 Example for POST Oauth:
```
{
    "email": "test@user.ru",
    "login": "test1",
    "social_id": "5464rghf65"
}
 ```
 
 respone:
```
"ok" or "Email or login already exist"
```
 
 ### Sign In, Forgot Password
```
POST     /api/signin -> Sign In
PUT     /api/signin - > Forgot Password
```

These keys are required to sign in a user:
```
login, password
```
Example for POST:
```
{
    "login": "test1",
    "password": "123Wertyq"
}
 ```
 In the response you will get a token:
 ```
 {
    "message": "ok",
    "access_token": "eyJ0eXAiOiJK",
    'user_id': "32"
}
```

Example PUT:
```
{
    "email": test@mail.ru
}
```
Response if ok:
```
We have sent a new passport to your email
```

 ### Log out
```
DELETE     /api/logout
```

### Users

```
GET     /api/users -> get all users
GET     /api/users/<user_id> -> get one user by id
PUT     /api/users/<user_id> -> update user's data
```

Response for getting one user:
```
    "user_id": 4,
    "login": "test",
    "email": "mr.andrey.sd@gmail.com",
    "info": "prefer horrors"
}

```

Columns that can be changed in PUT
```
['email', 'avatar', 'info']
```
NOTE: instead of JSON, use FormData


### Search

```
GET     /api/search?title=titanic&genre=Drama&minimum_rating=5 -> get video by title, genre or IMBD rating
```

Note: check key 'msg'. Response variants: ok, error, no movies found
```
{
    "msg": "ok",
    "movies": [
        {
        ...
        }
     ]
}
```

### Watch

```
GET     /api/watch/<torrent_id>
```
in response you get src to video

### Comments

```
GET     /api/comments?video_id=1
POST    /api/comments
```

response GET:
```
[
    {
        "comment_id": 1,
        "author": "Keker",
        "message": "asdasda",
        "creation_date": "01.01.2018 15:34",
        "video_id": 1
    }
]
```

request POST:
```
{
    "author": "Keker",
    "message": "asdasda",
    "creation_date": "01.01.2018 15:34",
    "video_id": 1
}
```

To test videos
download your video to backend/videos_hub

add it in backend/test_entities.py in array videos


