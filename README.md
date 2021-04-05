# WheaterAPI

## RUN REDIS CONTAINER

docker run -d --name redis-container -p 6379:6379 redis

## RUN APP CONTAINER AND LINK IT WITH REDIS

docker run -it --name app -p 8080:8080 --link redis-container weatherapp/python