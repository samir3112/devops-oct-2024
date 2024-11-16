FROM python:3.12-slim
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# for named volume we don't need this
# this will be done with command
# VOLUME [ "/app/userchanges" ]

CMD ["flask", "run", "--host", "0.0.0.0"]


# docker volume prune
# docker volume ls
# docker build -t cbagade/py-data-vol:v3 .
# docker push cbagade/py-data-vol:v3
# docker run -p 5000:5000 -d --name named-vol -v namedvol:/app/userchanges --rm cbagade/py-data-vol:v3
# docker ps -a
# observe a volume created
# docker volume ls
# docker exec -it named-vol /bin/bash
# cd userchanges
# make some changes to file on your computer (touch chandra.txt)
# docker stop named-vol
# ensure container is deleted
# docker ps -a
# docker run -p 5000:5000 -d --name named-vol -v namedvol:/app/userchanges --rm cbagade/py-data-vol:v3
# docker exec -it named-vol /bin/bash
# check the changes and this time changes are retained
# named volumes survives container restarts

# POST data
# curl 'http://localhost:5000/api/v1/fruits' --header 'Content-Type: application/json'  --data '{"fruitName":"Safarchand","from":"Kashmir","nutrients":"Vitamin B, Vitamin K","price":"210.50","organic":false,"description":"Safarchad is tasty fruit and keep doctor away"}'


# this action will create a file inside container
# GET  data
# curl  'http://localhost:5000/api/v1/fruits'

# docker stop named-vol
# ensure container is deleted
# docker ps -a

# docker run -p 5000:5000 -d --name named-vol -v namedvol:/app/userchanges --rm cbagade/py-data-vol:v3
# GET  data
# curl  'http://localhost:5000/api/v1/fruits'

# changes are retained
# docker stop named-vol

# delete volume 
# docker volume rm namedvol
# docker volume ls
