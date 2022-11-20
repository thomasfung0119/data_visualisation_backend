## Flask API Server

> Start the app in Docker

```bash
$ docker-compose pull   # download dependencies 
$ docker-compose build  # local set up
$ docker-compose up     # start the app 
```

Visit `http://localhost:5000` in your browser. The app should be up & running.

## How to use the code
**Step #0** - change the Keys
api/config.py
    -SECRET_KEY
    -JWT_SECRET_KEY

**Step #1** - create virtual environment using python3 and activate it (keep it outside our project directory)
$ # Linux
$ virtualenv env
$ source env/bin/activate
$
$ # Windows
$ virtualenv env
$ .\env\Scripts\activate

**Step #3** - Install dependencies in virtualenv
$ pip install -r requirements.txt

**Step #3** - setup `flask` command for our app
$ # Linux
$ export FLASK_APP=run.py
$ export FLASK_ENV=development
$ # Windows
$ $env:FLASK_APP = ".\run.py"
$ $env:FLASK_ENV = "development"

**Step #4** - start test APIs server at `localhost:5000`
$ flask run


## Project Structure
api-server-flask/
├── api
│   ├── config.py
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
├── Dockerfile
├── README.md
├── requirements.txt
├── run.py
└── tests.py


## API
> **Register** - `api/users/register` (**POST** request)

POST api/users/register
Content-Type: application/json

{
    "username":"test",
    "password":"pass", 
    "email":"test@appseed.us"
}


> **Login** - `api/users/login` (**POST** request)

POST /api/users/login
Content-Type: application/json

{
    "password":"pass", 
    "email":"test@appseed.us"
}
```

> **Logout** - `api/users/logout` (**POST** request)

POST api/users/logout
Content-Type: application/json
authorization: JWT_TOKEN (returned by Login request)

{
    "token":"JWT_TOKEN"
}

## Modules

This application uses the following modules

 - Flask==1.1.4
 - flask-restx==0.4.0
 - Flask-JWT-Extended
 - pytest

## Testing

Run tests using `pytest tests.py`

