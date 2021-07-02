# Sekigae Service


## 実行までの手順
dockerとdocker-composeインストール済みが前提

1. `git clone`する

1. 環境変数ファイルを追加（slackでもらう）

   1. `django/`内に`.env`を追加
   1. `postgres/`内に`.env`を追加

1. `django/entrypoint.sh`に実行権限を与える

   ```
   chmod +x django/entrypoint.sh
   ```
   このとき、それぞれのgitの設定によっては権限変更がgitに追跡されるので、gitの設定を変更する(エラー出た人だけでいいよ)  
   `git config core.filemode false`

1. docker起動

   ```
   docker-compose up -d --build
   ```

1. http://localhost:8000/ にアクセス

1. ロケットが飛んでたら成功！おめでとう！
