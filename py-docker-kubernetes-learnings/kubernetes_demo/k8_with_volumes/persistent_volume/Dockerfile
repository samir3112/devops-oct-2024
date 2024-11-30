FROM python:3.12-slim
RUN apt update -y && apt install curl -y
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV PYTHONUNBUFFERED=1
CMD ["flask", "run", "--host", "0.0.0.0"]