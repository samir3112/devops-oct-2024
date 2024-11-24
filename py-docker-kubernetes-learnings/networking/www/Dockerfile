FROM python:3.12-slim
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
CMD ["flask", "run", "--host", "0.0.0.0"]


# docker build -t cbagade/py-networking:v1 .
# docker run -p 5000:5000 -d --name network-app --rm cbagade/py-networking:v1
# on postman
# http://localhost:5000/movies
# shows OOB container to outside world communication works