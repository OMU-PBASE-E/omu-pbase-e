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
