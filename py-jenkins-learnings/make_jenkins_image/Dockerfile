FROM jenkins/jenkins:lts

USER root
RUN apt-get update -y
RUN curl https://get.docker.com/ > dockerinstall \
    && chmod 777 dockerinstall \
    && ./dockerinstall

RUN usermod -aG docker jenkins

RUN apt-get update -y \
    && apt-get install python3 -y \
    && apt-get install python3-pip -y \
    && apt install python3.11-venv -y \
    && rm -rf /usr/lib/python3.11/rm EXTERNALLY-MANAGED


USER jenkins

# https://faun.pub/how-to-install-docker-in-jenkins-container-4c49ba40b373
# docker build -t cbagade/jenkins:v1 .
# sudo chmod 666 /var/run/docker.sock
# remove previous jenkins volume
# docker volume prune
# docker run -p 8080:8080 -p 50000:50000 -d -v /var/run/docker.sock:/var/run/docker.sock -v jenkins_home:/var/jenkins_home cbagade/jenkins:v1


# on vagrant fo port fwding
# docker ps -a
# docker exec -it 2b335b6af87b bash -c 'cat /var/jenkins_home/secrets/initialAdminPassword'

# run with ngroks
# ngrok http 80
# Or
# docker run -it -e NGROK_AUTHTOKEN=<token> ngrok/ngrok http <Jenkins_container_if>:8080

# For k8 integration
# https://www.hatica.io/blog/ci-cd-pipeline-with-jenkins-and-kubernetes/
# don't use following
# docker run -p 8080:8080 -p 50000:50000 -d -v /var/run/docker.sock:/var/run/docker.sock -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts