# base image, this will provide a python environment for out application to run
# slim version of python image
FROM python:3.12-slim

# install curl 
RUN apt update -y && apt install curl -y

# expose 5000 port of container, to map the port of our application
EXPOSE 5000

# on to OS of above base image, we saying /app should be our working directory
# its like cd /app
WORKDIR /app

# copy requirements.txt file from local machine in /app directory
COPY requirements.txt .

# run pip install -r requirements.txt to install libraries
RUN pip install -r requirements.txt

# copy everything to /app directory inside container
COPY . .

# for print statements
ENV PYTHONUNBUFFERED=1

# command to run on container
# server accepts request from all hosts
CMD ["flask", "run", "--host", "0.0.0.0"]


# docker build -t cbagade/py-kube-setup:v1 .
# docker push cbagade/py-kube-setup:v1

# pods


# kubectl run app --image=cbagade/py-kube-setup:v1   -> deploys docker container by creating a pod
# kubectl get pods -> lists the pod
# kubectl describe pod <pod_name>
# kubectl delete pod <pod_name>



# Deployment
# the images should be pushed in repository
# kubectl create deployment kube-setup --image=cbagade/py-kube-setup:v1
# kubectl get deployment
# kubectl get pods
# kubectl describe pod <pod_name>
# Get Pod IP
# kubectl get pod -o wide
# Delete deployment
# kubectl delete deployment <deployment_name>
# kubectl create deployment kube-setup --image=cbagade/py-kube-setup:v1
# Get Pod IP
# kubectl get pod -o wide
# It will change


# Calling this app
# try curl http://localhost:5000/greetings -> fails
# try to get IP Address of pod
# kubectl get pod -o wide
# try curl http://172.16.140.89:5000/greetings
# enter inside container
# kubectl exec -it <pod> -- /bin/bash
# curl http://10.244.0.17:5000/greetings -> success
# The pod ip is reachable inside cluster only


# Service
# NodePort (can't specify exact nodeport on cli)
# kubectl expose --type=NodePort deployment kube-setup --port 5000 --name kube-setup
# nodeport will automatically be assigned
# kubectl get svc
# curl http://localhost:<nodeport>/greetings/error
# observe pod going from error to running to error
# kubectl get pods -w
# the pods to running will go due to Deployment, it will try to bring up the pod
# curl http://localhost:<nodeport>/greetings
# this will ensure pod in running state
# kubectl delete svc <svc_name>


# ClusterIP
# For pods to communicate with other pods within cluster
# With ClusterIP service , pods can't be reached from outside
# kubectl expose --type=ClusterIP  deployment kube-setup --port 5000 --name kube-setup
# kubectl get svc
# Get IP of svc
# curl http://<svc_ip>:5000/greetings  ,  accessible
# Enter inside pod 
# kubectl get pods
# kubectl exec -it <pod_name> -- /bin/bash
# curl http://<svc_ip>:5000/greetings  ,  accessible (inside cluster)
# But again this will be reachable from within cluster, try entering pod and execute curl
# kubectl get svc
# kubectl delete svc <svc_name>



# Scaling (open 3 terminal windows)
# kubectl get pods -w --> 1 terminal
# kubectl scale deployment/kube-setup --replicas=3 --> 2 terminal
# observe pod on 1 terminal increasing to 3
# curl http://localhost:30008/greetings --> 3 terminal, can be served from any of these pods
# curl http://localhost:30008/greetings/error --> 2 terminal and hit immediately
# curl http://localhost:30008/greetings --> 3 terminal
# there won't be error because now request will go to other healthy pod


# Deleting
# kubectl delete svc kube-setup
# kubectl delete deployment kube-setup


# Dashboard, At moment not working on vagrant
# kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
# OR access URL in browser,  save the content in dashboard.yaml and kubectl apply -f dashboard.yaml
# kubectl get pod -n kubernetes-dashboard
# kubectl create serviceaccount -n kubernetes-dashboard admin-user
# kubectl create clusterrolebinding -n kubernetes-dashboard admin-user --clusterrole cluster-admin --serviceaccount=kubernetes-dashboard:admin-user
# token=$(kubectl -n kubernetes-dashboard create token admin-user)
# echo $token
# kubectl proxy
# Access following URL in browser
# http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/
# input the token
# create deployment and service again and observe in UI. Don't forget to change namespace

# dry run
# kubectl run app --image=cbagade/py-kube-setup:v1 --dry-run=client -o yaml
# kubectl create deployment kube-setup --image=cbagade/py-kube-setup:v1 --dry-run=client -o yaml
# kubectl expose --type=ClusterIP  deployment kube-setup --port 5000 --name kube-setup --dry-run=client -o yaml