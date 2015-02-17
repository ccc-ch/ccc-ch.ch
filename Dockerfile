FROM debian:stable
MAINTAINER hp@oeri.ch

ENV DEBIAN_FRONTEND noninteractive
ENV LANG            C.UTF-8

RUN	sed -ri 's@http://http.debian.net/@ftp://ftp.ch.debian.org/@' \
	/etc/apt/sources.list
RUN     apt-get -qqy update && \
	apt-get install -y sudo python-pip && \
        apt-get -qqy clean

ADD     requirements.txt /tmp/
RUN     pip install -r /tmp/requirements.txt

RUN     rm -rf /var/lib/apt/lists/* 

EXPOSE 8000
ENTRYPOINT /var/www/run.sh
