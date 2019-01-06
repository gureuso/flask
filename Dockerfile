FROM centos:7
MAINTAINER gureuso <gureuso.github.io>

USER root
WORKDIR /root

# base
RUN yum update -y
RUN yum install -y epel-release
RUN yum install -y git python-pip python-devel gcc

# mysql
RUN rpm -ivh https://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm
RUN yum -y install mysql-community-server mysql-community-devel

# flask
RUN git clone https://github.com/gureuso/Flask.git
WORKDIR /root/Flask
RUN pip install virtualenv
RUN virtualenv venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt
RUN python manage.py test

CMD python manage.py runserver

EXPOSE 80