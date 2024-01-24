# omu-pbase-e

## How to run

以下のうちのいずれかを実行してください．
実行後は http://localhost:8000/ にアクセスすることでアプリケーションを表示できます．

### docker-compose

```sh
docker-compose up
```

### docker

```sh
docker build -t pbase .
docker run -it -p 8000:8000 --mount type=bind,source="$(pwd)/advanced_software/introduced_facility,target=/app" pbase
```

## データベースへの要素の追加の仕方
http://localhost:8000/admin/ で管理画面に入ってください。もし画面ユーザネームとパスワードを要求されたら、
ユーザネーム : okada
パスワード : 123
で行けると思います。