# RESTful API Matcha

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
GET     /api/search?video=titanic -> get video by name
POST    /api/search -> detailed search video
```

Example for POST:
```
{
    "genre": "fantasy",
    "year": 2018
}
