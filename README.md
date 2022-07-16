# fastapi-chemex-api
fastapi-chemex-api



docker run -dit \
  -p 8000:8000 \
  -e DB_HOST=XXX.XXX.XXX.XXX \
  -e DB_PORT=3306 \
  -e DB_NAME=chemex \
  -e DB_USERNAME=root \
  -e DB_PASSWORD=root \
  --name chemexapi \
  --hostname chemexapi \
  --restart unless-stopped \
  84896150/fastapi-chemex-api:latest

![This is an image](/QQ截图20220716101817.jpg)
