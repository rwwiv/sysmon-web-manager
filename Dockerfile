# Development docker image
FROM ubuntu:latest
LABEL maintainer="william.wernert@gmail.com"

# Python + pip setup
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
	git \
	sudo \
	curl \
	python3 \
	python3-dev \
	python3-setuptools \
	python3-pip \
	g++ \
	build-essential \
	supervisor \
	sqlite3 && \
	pip3 install -U pip setuptools && \
   	rm -rf /var/lib/apt/lists/*

RUN curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
RUN apt-get install -y nodejs

# Environment setup
ARG IP_ADDRESS
ENV API_PORT="8000"
ENV API_URL="http://$IP_ADDRESS:$API_PORT"
COPY ./server/backend /backend
COPY ./server/frontend /frontend
WORKDIR /frontend
RUN npm install -g @vue/cli
RUN npm install
WORKDIR /backend
RUN pip3 install -r requirements.txt
RUN python3 manage.py migrate

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord"]
