## Start the app in Docker

```bash
$ docker-compose pull   # download dependencies 
$ docker-compose build  # local set up
$ docker-compose up     # start the app 
```

Visit `http://localhost:5000` in your browser. The app should be up & running.

## Start the app without Docker

**Step #1** - create virtual environment using python3 and activate it (keep it outside our project directory)
```bash
$ # Linux
$ virtualenv env
$ source env/bin/activate
$
$ # Windows
$ virtualenv env
$ .\env\Scripts\activate
```

**Step #3** - Install dependencies in virtualenv

```bash
$ pip install -r requirements.txt
```

**Step #3** - setup `flask` command for our app
```bash
$ # Linux
$ export FLASK_APP=run.py
$ export FLASK_ENV=development
$ # Windows
$ $env:FLASK_APP = ".\run.py"
$ $env:FLASK_ENV = "development"
```

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

## Testing

Run tests using `pytest tests.py`

