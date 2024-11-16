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
# run mongo db with named volume
# docker network create demo-net
# docker run -d --name mongodb -v data:/data/db --rm --network demo-net --rm mongo:4.4
# docker build -t cbagade/py-networking:v4 .
# docker run -p 5000:5000 -d --name network-app --network demo-net --rm cbagade/py-networking:v4


# GET DATA (fetch nothing)
# curl http://localhost:5000/api/v1/fruits 
# POST DATA
# curl 'http://localhost:5000/api/v1/fruits' --header 'Content-Type: application/json'  --data '{"fruitName":"Safarchand","from":"Kashmir","nutrients":"Vitamin B, Vitamin K","price":"210.50","organic":false,"description":"Safarchad is tasty fruit and keep doctor away"}'
# curl http://localhost:5000/api/v1/fruits 
# docker stop mongodb
# docker run -d --name mongodb -v data:/data/db --rm --network demo-net mongo:4.4
# now GET request will show previous data, hence proved , data is persisted
# curl http://localhost:5000/api/v1/fruits 
# docker stop network-app
# docker stop mongodb
# docker network ls
# docker network rm demo-net