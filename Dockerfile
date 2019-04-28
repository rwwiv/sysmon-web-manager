# Development docker image
FROM node:10-alpine
LABEL maintainer="william.wernert@gmail.com"

# Python + pip setup

RUN apk add --no-cache --update python3 \
	python3-dev \
	py3-setuptools \
	git \
	sudo \
	curl \
	gcc \
	g++ \
	make \
	sqlite \
	bash \
	supervisor && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

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

ENTRYPOINT ["supervisord", "--nodaemon", "--configuration", "/etc/supervisor/conf.d/supervisord.conf"]
