MAINTAINER William Wernert <william.wernert@gmail.com>

# Build frontend VueJS project for deployment
FROM node:alpine AS frontend
COPY ./server/frontend /frontend
WORKDIR /frontend
RUN npm install -g @vue/cli
RUN npm install
RUN npm run build

# Set up production environment
FROM ubuntu:18.04
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
	git \
	python3 \
	python3-dev \
	python3-setuptools \
	python3-pip \
	nginx \
	supervisor \
	sqlite3 && \
	pip3 install -U pip setuptools && \
   rm -rf /var/lib/apt/lists/*
# Set up Django
COPY /server/backend /backend
WORKDIR /backend
RUN pip3 install -r requirements.txt
RUN python3 manage.py runserver 0.0.0.0:8000

# Copy built frontend from previous image
COPY --from=frontend /frontend/dist /frontend/dist
# Set up nginx
COPY nginx.conf /etc/nginx/sites-available/default

