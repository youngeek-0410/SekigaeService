FROM python:3.8.3

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /src

RUN apt-get update && apt-get install -y --no-install-recommends netcat less gosu

# pipを使ってpoetryをインストール
RUN pip install poetry

# poetryの定義ファイルをコピー (存在する場合)
COPY pyproject.toml* poetry.lock* ./

# poetryでライブラリをインストール (pyproject.tomlが既にある場合)
RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install; fi

COPY . .

# uvicornのサーバーを立ち上げる
ENTRYPOINT ["/src/entrypoint.sh"]