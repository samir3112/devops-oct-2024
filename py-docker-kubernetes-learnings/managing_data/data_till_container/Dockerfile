FROM python:3.12-slim
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
# copy everything to /app directory inside container
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]


# docker build -t cbagade/py-data-vol:v1 .
# docker run -d  -p 5000:5000 --name manage-data --rm cbagade/py-data-vol:v1 (--rm flag will remove container when its not running)
# docker logs manage-data -f

# GET  data
# curl  'http://localhost:5000/api/v1/fruits'
# POST data
# curl 'http://localhost:5000/api/v1/fruits' --header 'Content-Type: application/json'  --data '{"fruitName":"Safarchand","from":"Kashmir","nutrients":"Vitamin B, Vitamin K","price":"210.50","organic":false,"description":"Safarchad is tasty fruit and keep doctor away"}'
# GET  data
# curl  'http://localhost:5000/api/v1/fruits'
# docker stop manage-data
# docker run -p 5000:5000 -d --name manage-data --rm cbagade/py-data-vol:v1
# GET  data
# curl  'http://localhost:5000/api/v1/fruits'
# data was available till container was running