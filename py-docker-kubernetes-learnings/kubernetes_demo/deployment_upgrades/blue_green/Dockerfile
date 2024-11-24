FROM python:3.12-slim
RUN apt update -y && apt install curl -y
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED=1
CMD ["flask", "run", "--host", "0.0.0.0"]


# docker build -t cbagade/dep-up-app:v1 .
# docker push cbagade/dep-up-app:v1
# change something in app
# docker build -t cbagade/dep-up-app:v2 .
# docker push cbagade/dep-up-app:v2