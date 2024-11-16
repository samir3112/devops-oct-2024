FROM python:3.12-slim
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]


# docker stop network-app
# docker stop mongodb
# docker rm mongodb
# prior that lets run mongo container
# docker run -d --name mongodb mongo:4.4
# see mongo container running
# docker ps -a
# docker inspect mongodb
# look for "NetworkSettings" -> "IPAddress"
# change mongo_pass.py for IP
# docker build -t cbagade/py-networking:v2 .
# docker run -p 5000:5000 -d --name network-app --rm cbagade/py-networking:v2
# docker logs network-app -f
# ensure content type from postman is JSON
# GET DATA (fetch nothing)
# curl http://localhost:5000/api/v1/fruits 
# POST DATA
# curl 'http://localhost:5000/api/v1/fruits' --header 'Content-Type: application/json'  --data '{"fruitName":"Safarchand","from":"Kashmir","nutrients":"Vitamin B, Vitamin K","price":"210.50","organic":false,"description":"Safarchad is tasty fruit and keep doctor away"}'
# curl http://localhost:5000/api/v1/fruits 
# docker stop network-app
# docker stop mongodb
# docker rm mongodb
