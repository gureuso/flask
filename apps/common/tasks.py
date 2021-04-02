from time import sleep
from urllib.parse import quote_plus
from celery import Celery

app = Celery('tasks', broker='sqs://{}:{}@'.format('AKIATE6L2P5UMLPGWLHR',
                                                   quote_plus('Me1BFxFtoyi8ddZOhfnA+zkN0Ag/D1gja72ZVrH/')))


@app.task
def hello():
    sleep(1)
    return 'hello world'
