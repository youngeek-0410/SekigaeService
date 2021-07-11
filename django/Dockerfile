# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/app

# Pythonがpyc filesとdiscへ書き込むことを防ぐ
ENV PYTHONDONTWRITEBYTECODE 1
# # Pythonが標準入出力をバッファリングすることを防ぐ
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk add \
    gcc \
    make \
    python3-dev \
    musl-dev \
    libffi-dev \
    mariadb-dev \
    postgresql-dev \
    g++ \
    libgcc \
    libstdc++ \
    libxml2-dev \
    libxslt-dev \
    jpeg-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]