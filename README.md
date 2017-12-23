# Flask
Flask simple example

# Usage

install virtualenv
```sh
$ pip install virtualenv
$ mkdir venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

run flask server
```sh
$ python manage.py runserver
```
if you do not install database you can get the database connection error

# Test
```sh
python manage.py test
```

# Migrate
if you want to use Flask-Migrate you enter this command
```sh
$ python manage.py db
```

- [Flask-Migrate docs](https://flask-migrate.readthedocs.io/en/latest/)

# ENV

| Name                | Description                      |
| ------------------- | -------------------------------- |
| APP_MODE            | choose from production, development, testing |
| APP_HOST            | ip address                       |
| APP_PORT            | port number                      |
| MYSQL_USER_NAME     | mysql user name                  |
| MYSQL_USER_PASSWD   | mysql user password              |
| MYSQL_HOST          | mysql host                       |
| MYSQL_DB_NAME       | mysql db name                    |
| REDIS_HOST          | redis ip address                 |
| REDIS_PASSWD        | redis password                   |
