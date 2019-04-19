FROM centos:7
MAINTAINER gureuso <gureuso.github.io>

USER root
WORKDIR /root

# base
RUN yum update -y
RUN yum install -y epel-release
RUN yum install -y git gcc

# python
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm
RUN yum install -y python36u python36u-devel python36u-libs python36u-pip
RUN ln -s /bin/python3.6 /bin/python3
RUN ln -s /bin/pip3.6 /bin/pip

# mysql
RUN yum -y install http://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm
RUN yum -y install mysql-community-client mysql-community-devel

# flask
RUN git clone https://github.com/gureuso/flask.git
WORKDIR /root/flask
RUN pip install virtualenv
RUN virtualenv -p python3 venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt

CMD python3 manage.py runserver

EXPOSE 80