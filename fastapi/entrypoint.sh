#!/bin/bash

if [ "$DB" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

cd /src/db
poetry run alembic upgrade head
poetry run python seed.py

cd /src
poetry run uvicorn app.main:app --host 0.0.0.0 --reload

exec $cmd