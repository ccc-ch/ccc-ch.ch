FROM ubuntu:14.04
MAINTAINER hp@oeri.ch

ENV DEBIAN_FRONTEND noninteractive
ENV LANG            C.UTF-8

RUN apt-get -qqy update && \
    apt-get install -y ruby nodejs npm && \
    apt-get -qqy clean
RUN rm -rf /var/lib/apt/lists/* 

ADD package.json /tmp/
RUN npm install --quiet -g grunt-cli
RUN cd /tmp && npm install --quiet
RUN gem install sass scss-lint

WORKDIR /var/www/site
CMD grunt watch
# TODO remove run.sh
