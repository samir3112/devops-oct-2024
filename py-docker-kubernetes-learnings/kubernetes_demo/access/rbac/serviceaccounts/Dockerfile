FROM python:3.12-slim
RUN apt update -y && apt install curl -y
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV PYTHONUNBUFFERED=1
CMD ["flask", "run", "--host", "0.0.0.0"]


# docker build -t cbagade/sa-demo:v1 .
# docker push cbagade/sa-demo:v1

# kubectl create -f pod_1.yaml -f pod_2.yaml
# enter in pod 1
# kubectl exec -it app-1 -n kube-learnings -- bash
# pod use default serviceaccount if not specified which got token and certificate to call kube-apiserver
# Follow below commands, to call kube-apiserver


# Export the internal Kubernetes API server hostname 
# APISERVER=https://kubernetes.default.svc 

# Export ServiceAccount
# SERVICEACCOUNT=/var/run/secrets/kubernetes.io/serviceaccount 
# echo $SERVICEACCOUNT

# Export ServiceAccount bearer token 
# TOKEN=$(cat ${SERVICEACCOUNT}/token) 
# echo $TOKEN

# Export nternal Kubernetes certificate authority (CA) 
# CACERT=${SERVICEACCOUNT}/ca.crt 
# echo $CACERT

# Make a call to the Kubernetes API with TOKEN 
# curl --cacert ${CACERT} --header "Authorization: Bearer ${TOKEN}" -X GET ${APISERVER}/api/v1/namespaces/default/pods 

# this will give error, because the default service account don't have much permissions

# now create custom servive account and give permissions
# kubectl create -f sa.yaml

# create pod role
# kubectl apply -f pod_reader.yaml

# create role bindings with service accounts
# kubectl apply -f role_bdg.yaml

# create pod 3 with service account
# kubectl apply -f pod_3.yaml

# kubectl exec -it app-3 -n kube-learnings -- bash
# repeat same steps to get pods
# APISERVER=https://kubernetes.default.svc 
# SERVICEACCOUNT=/var/run/secrets/kubernetes.io/serviceaccount 
# TOKEN=$(cat ${SERVICEACCOUNT}/token) 
# CACERT=${SERVICEACCOUNT}/ca.crt 
# curl --cacert ${CACERT} --header "Authorization: Bearer ${TOKEN}" -X GET ${APISERVER}/api/v1/namespaces/kube-learnings/pods 

# delete everything
# kubectl delete -f pod_1.yaml -f pod_2.yaml -f pod_3.yaml -f pod_reader.yaml -f role_bdg.yaml -f sa.yaml