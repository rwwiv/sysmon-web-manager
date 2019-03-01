FROM ubuntu:18.04
MAINTAINER William Wernert <william.wernert@gmail.com>

RUN apt update
RUN apt upgrade -y

RUN mkdir -p /server
WORKDIR /server
COPY server .

WORKDIR /server/backend
RUN apt install -y python3 python3-setuptools python3-pip
RUN pip3 install -r requirements.txt

WORKDIR /server/frontend
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash

#This is not finished
