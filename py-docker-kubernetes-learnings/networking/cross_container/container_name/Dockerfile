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
# docker network create demo-net
# docker network ls
# docker run -d --name mongodb --network demo-net --rm mongo:4.4
# mongo_pass.py will have now name of mongo container instead of IP Address
# docker build -t cbagade/py-networking:v3 .
# docker run -p 5000:5000 -d --name network-app --network demo-net --rm cbagade/py-networking:v3

# GET DATA (fetch nothing)
# curl http://localhost:5000/api/v1/fruits 
# POST DATA
# curl 'http://localhost:5000/api/v1/fruits' --header 'Content-Type: application/json'  --data '{"fruitName":"Safarchand","from":"Kashmir","nutrients":"Vitamin B, Vitamin K","price":"210.50","organic":false,"description":"Safarchad is tasty fruit and keep doctor away"}'
# curl http://localhost:5000/api/v1/fruits 
# docker stop network-app
# docker stop mongodb
# docker network rm demo-net