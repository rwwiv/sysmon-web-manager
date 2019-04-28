# SysMonager
Web management interface for enterprise sysmon deployments

[![Build Status](https://travis-ci.com/rwwiv/sysmon-web-manager.svg?branch=master)](https://travis-ci.com/rwwiv/sysmon-web-manager)
[![Build status](https://ci.appveyor.com/api/projects/status/qw9fme4a90kev148?svg=true)](https://ci.appveyor.com/project/rwwiv/sysmon-web-manager)

## Prerequisites

The following software is needed in order to run the server locally:
* Python 3 + pip
* NodeJS + npm 
* Vue CLI `npm install @vue/cli`

The docker image requires only Docker to be installed.

## Environment Variables
* **API_PORT** - defines the port that the Django api server will listen on (default is 8000)
* **API_URL** - defines the url that directs to the Django api server

## Local Development

### Server

There are two methods to run the development server:

* Docker

``` sh
docker built . -t sysmonager --build-arg IP_ADDRESS=<host IP>
docker run -d -p 8000:8000 -p 8080:8080 <container name> sysmonager
```

* Localhost

``` sh
# in <repository>/server/backend
pip install -r requirements.txt
# if a clean db is needed you can delete db.sqlite3 on subsequent runs
python manage.py migrate
python manage.py runserver
```
> In another terminal window

``` sh
# in <repository>/server/frontend
export API_PORT=8000
export API_URL=http://localhost:$API_PORT
npm install
npm run serve
```

### Agent

The agent must be run on a Windows computer since we're managing a Windows only tool.

**\*BEFORE FIRST RUN\*** make sure the config.ini is pointing to the server URL you have set up (for development this will usually be the host IP if running the server through docker or localhost otherwise)

``` pwsh 
# in <repository>/agent
python install -r requirements.txt
cd agent
python .\__init__.py
```
