FROM python:3.12-slim

# install curl 
RUN apt update -y && apt install curl -y
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV PYTHONUNBUFFERED=1
CMD ["flask", "run", "--host", "0.0.0.0"]


# docker build -t cbagade/pykubd-first-app:v5 .
# docker push cbagade/pykubd-first-app:v5