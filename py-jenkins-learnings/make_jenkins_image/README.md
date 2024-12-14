## https://faun.pub/how-to-install-docker-in-jenkins-container-4c49ba40b373

docker build -t cbagade/jenkins:v1 .

sudo chmod 666 /var/run/docker.sock

docker run -p 8080:8080 -p 50000:50000 -d -v /var/run/docker.sock:/var/run/docker.sock -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts

on vagrant do port fwding

docker exec -it e9bddb892c7c bash -c 'cat /var/jenkins_home/secrets/initialAdminPassword'

run with ngroks

docker run -it -e NGROK_AUTHTOKEN=<token> ngrok/ngrok http <Jenkins_container_if>:8080