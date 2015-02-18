FROM ubuntu:14.04
MAINTAINER hp@oeri.ch

ENV DEBIAN_FRONTEND noninteractive
ENV LANG            C.UTF-8

RUN apt-get -qqy update && \
    apt-get install -y sudo python-dev python-pip && \
    apt-get -qqy clean
RUN rm -rf /var/lib/apt/lists/* 

ADD requirements.txt /tmp/
RUN pip install -U -r /tmp/requirements.txt

EXPOSE 8000
ENTRYPOINT /var/www/.docker/pelican/run.sh
