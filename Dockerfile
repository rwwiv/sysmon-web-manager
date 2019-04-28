# Development docker image
FROM nikolaik/python-nodejs:latest
LABEL maintainer="william.wernert@gmail.com"
COPY ./server /
COPY ./start.sh /
COPY ./env.sh /
WORKDIR /frontend
RUN npm install -g @vue/cli
RUN npm install
WORKDIR /backend
RUN pip install -r requirements.txt

ENTRYPOINT [ ". /env.sh && /start.sh" ]
