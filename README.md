# Flask
Flask simple example

# Usage

### 1. install virtualenv
```sh
$ pip install virtualenv
$ mkdir venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

### 2. set environment
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

### 3. db migrate
```sh
$ python manage.py db migrate
$ python manage.py db upgrade
```
migrate db tables

### 4. run test code
```sh
$ python manage.py test
```

### 5. run flask server
```sh
$ python manage.py runserver
```
if you do not install database, you can get the database connection error.

# Command

### runserver
```sh
$ python manage.py runserver
```

optional arguments:
```sh
-h, --host  hostname
-p, --port  port number
```

run flask server

### test
```sh
$ python manage.py test
```
run test code with unittest2


### db
```sh
$ python manage.py db
usage: Perform database migrations

Perform database migrations

positional arguments:
  {init,revision,migrate,edit,merge,upgrade,downgrade,show,history,heads,branches,current,stamp}
    init                Creates a new migration repository
    revision            Create a new revision file.
    migrate             Alias for 'revision --autogenerate'
    edit                Edit current revision.
    merge               Merge two revisions together. Creates a new migration
                        file
    upgrade             Upgrade to a later version
    downgrade           Revert to a previous version
    show                Show the revision denoted by the given symbol.
    history             List changeset scripts in chronological order.
    heads               Show current available heads in the script directory
    branches            Show current branch points
    current             Display the current revision for each database.
    stamp               'stamp' the revision table with the given revision;
                        don't run any migrations

optional arguments:
  -?, --help            show this help message and exit
```
perform database migrations

https://flask-migrate.readthedocs.io/en/latest/

# Docker

support the docker. however, you need to install database server. below is an example of database dockerfile.

```dockerfile
FROM mysql:5.7
MAINTAINER gureuso <gureuso.github.io>

USER root

ENV MYSQL_ROOT_PASSWORD asdf1234
ENV MYSQL_DATABASE flask

EXPOSE 3306
```