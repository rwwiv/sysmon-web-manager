#!/bin/bash
## Development script

# Set up backend
cd server/backend
pip install -r requirements.txt
if [ -f "db.sqlite3" ]; then rm "db.sqlite3"; fi
python manage.py migrate

# Set up frontend
cd ../frontend
npm install
# optionally, lint all javascript in the npm project
# npm run lint

# Run server
cd ../backend
python manage.py runserver 0.0.0.0:$API_PORT
cd ../frontend
npm run serve



