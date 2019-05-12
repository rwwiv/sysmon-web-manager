# Development docker image

# Image builds VueJs frontend
FROM node:10-alpine AS frontend
RUN apk add --no-cache --update \
	git \
	sudo \
	curl \
	gcc \
	g++ \
	make \
	bash 
COPY ./frontend /
RUN npm install && npm run build


# Final image
FROM python:alpine
LABEL maintainer="william.wernert@gmail.com"

# Set Python environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Init Django server
COPY ./server/backend /backend
WORKDIR /backend
RUN pip install -r requirements.txt
RUN python manage.py migrate

# Set up nginx to serve frontend
RUN apk add --update nginx sqlite
RUN adduser -D -g 'www' www && \
	mkdir /www && \
	chown -R www:www /var/lib/nginx && \
	chown -R www:www /www
COPY --from=frontend /dist /frontend
COPY nginx.conf /etc/nginx/nginx.conf

# Copy supervisord config to manage django task
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ENTRYPOINT ["supervisord", "--nodaemon", "--configuration", "/etc/supervisor/conf.d/supervisord.conf"]
