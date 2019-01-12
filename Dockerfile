FROM centos:7
MAINTAINER gureuso <gureuso.github.io>

USER root
WORKDIR /root

# env
RUN echo 'APP_MODE: '$APP_MODE
RUN echo 'APP_HOST: '$APP_HOST
RUN echo 'APP_PORT: '$APP_PORT
RUN echo 'MYSQL_USER_NAME: '$MYSQL_USER_NAME
RUN echo 'MYSQL_USER_PASSWD: '$MYSQL_USER_PASSWD
RUN echo 'MYSQL_HOST: '$MYSQL_HOST
RUN echo 'MYSQL_DB_NAME: '$MYSQL_DB_NAME
RUN echo 'REDIS_HOST: '$REDIS_HOST
RUN echo 'REDIS_PASSWD: '$REDIS_PASSWD

# base
RUN yum update -y
RUN yum install -y epel-release
RUN yum install -y git python-pip python-devel gcc

# mysql
RUN yum -y install http://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm
RUN yum -y install mysql-community-client mysql-community-devel

# flask
RUN git clone https://github.com/gureuso/Flask.git
WORKDIR /root/Flask
RUN pip install virtualenv
RUN virtualenv venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt
RUN python manage.py db migrate
RUN python manage.py db upgrade
RUN python manage.py test

CMD python manage.py runserver

EXPOSE 80