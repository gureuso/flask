# Flask
Flask example

# Usage

### 1. install virtualenv
```sh
$ pip install virtualenv
$ virtualenv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

### 2. set environment or create config.json
| Name                | Description                      |
| ------------------- | -------------------------------- |
| APP_MODE            | choose from production, development, testing |
| APP_HOST            | ip address                       |
| APP_PORT            | port number                      |
| DB_USER_NAME        | db user name                     |
| DB_USER_PASSWD      | db user password                 |
| DB_HOST             | db host                          |
| DB_NAME             | db name                          |
| REDIS_HOST          | redis ip address                 |
| REDIS_PASSWD        | redis password                   |
| TESTING             | if using test table true else false |

### 3. db migrate
```sh
$ export FLASK_APP=apps.common.commands.manager
$ flask db stamp head
$ flask db migrate
$ flask db upgrade
```
migrate db tables

### 4. run test code
```sh
$ export FLASK_APP=apps.common.commands.manager
$ flask test
```

### 5. run flask server
```sh
$ python3 manage.py
```
if you do not install database, you can get the database connection error.

# Command

### test
```sh
$ export FLASK_APP=apps.common.commands.manager
$ flask test
```
run test code with unittest2


### db
```sh
$ export FLASK_APP=apps.common.commands.manager
$ flask db
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
