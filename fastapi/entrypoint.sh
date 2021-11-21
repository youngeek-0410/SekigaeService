#!/bin/bash

# DBとの接続を待つ
if [ "$DB" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# host PCと同じユーザーを作成してpermission問題を解決
USER_ID=${USER_ID:-1000}
GROUP_ID=${GROUP_ID:-1000}
USER_NAME=${USER_NAME:-developer}
echo "Creating user($USER_NAME) with UID : $USER_ID, GID: $GROUP_ID"
useradd -u $USER_ID -o -m $USER_NAME
groupadd -g $GROUP_ID $USER_NAME

# migration & seed
cd /src/app/db
poetry run alembic upgrade head
poetry run python seed.py

# fastapiサーバーの起動
cd /src
poetry run uvicorn app.main:app --host 0.0.0.0 --reload

exec /usr/sbin/gosu $USER_NAME "$@"