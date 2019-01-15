FROM centos:7
MAINTAINER gureuso <gureuso.github.io>

USER root
WORKDIR /root

# base
RUN yum update -y
RUN yum install -y epel-release
RUN yum install -y git python-pip python-devel gcc

# mysql
RUN yum -y install http://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm
RUN yum -y install mysql-community-client mysql-community-devel

# flask
RUN git clone https://github.com/gureuso/flask.git
WORKDIR /root/flask
RUN pip install virtualenv
RUN virtualenv venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt

CMD python manage.py runserver

EXPOSE 80