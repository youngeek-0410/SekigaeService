# Sekigae Service


## 実行までの手順
dockerとdocker-composeインストール済みが前提

1. `git clone https://github.com/youngeek-0410/SekigaeService.git`

1. `cd SekigaeService`

1. `source env.sh`

1. 環境変数ファイルを追加（slackでもらう）

   1. `django/`内に`.env`を追加
   1. `postgres/`内に`.env`を追加

1. `django/entrypoint.sh`に実行権限を与える

   ```
   chmod +x django/entrypoint.sh
   ```

1. docker起動

   ```
   build
   up
   ```

1. http://localhost/ にアクセス

1. ロケットが飛んでたら成功！おめでとう！

1. Ctrl + C でdocker停止

## 初回以降の起動
(env.shが読み込まれている状態で)
```
up
```
