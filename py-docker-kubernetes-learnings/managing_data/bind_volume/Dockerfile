FROM python:3.12-slim
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]


# docker stop named-vol
# docker volume prune
# docker volume rm namedvol
# docker build -t cbagade/py-data-vol:v4 .
# docker run -p 5000:5000 -d --name bind-vol -v "/home/vagrant/py-docker-kubernetes-learnings/managing_data/bind_volume/userchanges:/app/userchanges" --rm cbagade/py-data-vol:v4
# OR TRY THIS (newwer way)
# docker run -p 5000:5000 -d --name bind-vol --mount type=bind,source=/home/chandra/docker-kubernetes-learnings/managing_data/bind_volume/userchanges,target=/app/userchanges --rm cbagade/py-data-vol:v4
# docker volume won't list any volume
# docker volume ls
# GET  data
# curl  'http://localhost:5000/api/v1/demo_bind_vol'

# now this volume with be mounted on /home/chandra/docker-kubernetes-learnings/managing_data/named_volume/userchanges
# any changes made to file inside container will be available at this path
# not for production