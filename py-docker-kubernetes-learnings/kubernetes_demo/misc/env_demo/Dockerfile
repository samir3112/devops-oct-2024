FROM python:3.12-slim
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
CMD ["flask", "run", "--host", "0.0.0.0"]


# docker build -t cbagade/py-first-prog-env:v3 .
# docker push cbagade/py-first-prog-env:v3

# docker run -e "who_to_greet_env_var=DevOps Team" -d -p 5000:5000 cbagade/py-first-prog-env:v3
# http://localhost:5000/ (access application on host port which is mapped to container)

# docker run -e "who_to_greet_env_var=Softtronics Team" -d -p 5001:5000 cbagade/py-first-prog-env:v3
# http://localhost:5001/ (access application on host port which is mapped to container)


