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

   ```bash
   chmod +x django/entrypoint.sh
   ```

1. docker起動

   ```bash
   build
   up
   ```

1. <http://localhost/> にアクセス

1. ロケットが飛んでたら成功！おめでとう！

1. Ctrl + C でdocker停止

## 初回以降の起動

(env.shが読み込まれている状態で)

```bash
up
```

## linter/formatter初期設定

commit時にlinter/formatterが自動的に走るように設定をする。

1. pythonの環境をlocalに構築(OS,宗教によって環境構築の仕方が異なるので割愛)
1. node, npmの環境をlocalに構築(OS,宗教によって環境構築の仕方が異なるので割愛)
    - このプロジェクトではyarnではなnpmを用いる。深い理由はない。
1. root(README.mdと同階層)で`npm install`で必要なパッケージをインストール
    - `package-lock.json`は自分で編集してはいけないファイルであり、git管理をする必要があります。編集・消去しないでcommitしてください。
1. root(README.mdと同階層)で`pip install -r requirements.txt`で必要なパッケージをインストール

linter/formatterはstaged fileのみに走ります。linter/formatterを走らせたくない場合は、`--no-verify`をcommit時にオプションで指定してください。
