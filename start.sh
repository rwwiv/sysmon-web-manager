#!/bin/bash
## Development script

. /env.sh

# Set up and run backend
if [ -f "db.sqlite3" ]; then rm "db.sqlite3"; fi
python manage.py migrate
python manage.py runserver 0.0.0.0:$API_PORT

# Run frontend
cd ../frontend
npm run serve



