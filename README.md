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

run flask app
```sh
$ python run.py
```
if you do not install database you can get the database connection error

# Test
```sh
python run.py test
```

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
