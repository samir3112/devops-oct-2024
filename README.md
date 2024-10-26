# docker-env

## To bring machine up
   carry all instructions on gitbash

   ensure Oracle Virtual Box 7.0 is setup
   
   ensure Vagrant is setup

   ```
   git clone this repository
   cd docker-env
   vagrant up
   ```

   this machine will have docker installed

## To work with VSC
   on gitbash -> code.

   this will open VSC

   install the "Remote - SSH" extension on VSC

   on git bash type -

   vagrant ssh-config

   store the content on some file like docker-vm-config.txt (change name of host to Docker)

   on VSC - ctrl + shift + P

   Remote-SSH: Open SSH Configuration File -> Settings -> add the previous created file

   again on VSC - ctrl + shift + P - > Remote SSH: Connect to Host

   connect to Docker (host) and select Linux on pop-up

   VSC will be downloaded on vagrant  machine (with till download finish)

## Install python 3.11
   3.12 are having issues, so install 3.11

   open terminal on VSC and install python 3.11 as - 

   following stes are from  - https://linuxcapable.com/how-to-install-python-3-11-on-ubuntu-linux/

   ```
   sudo apt update
   sudo apt upgrade (enter Y and press tab and space bar to confirm OK when window pops up)
   sudo add-apt-repository ppa:deadsnakes/ppa -y
   sudo apt update
   sudo apt install python3.11 (press ok when populated with space bar)
   python3.11 --version
   sudo apt install python3-pip (press ok when populated with space bar)
   python3 --version (If this display version other than 3.11 , follow below steps)
   ```

## Steps to make 3.11 as default python version
   ```
   cd /usr/bin/
   ls -lrth python*
   sudo unlink python3
   sudo ln -s /usr/bin/python3.11 python3
   python3 --version
   python3 -m pip install --upgrade pip
   ```

## Ensure Docker
   ```
   docker --version
   docker login -u <docker_hub_user>  (enter dockerhub password on prompt)
   ```

## Import Docker-Kubernetes git repo now to work with 
   ```
   cd -
   git clone https://<git_user>:<git_password>@github.com/cbagade/py-docker-kubernetes-learnings.git
   on VSC - Explorer - Open /home/vagrant/py-docker-kubernetes-learnings/
   select linux platform when prompted
   Trust the author when prompted
   open app.py -> VSC might prompt to install python extension, install
   open Dockerfile -> VSC might prompt to install docker extension, install
   ```
## Confirm python setup
   open Terminal
   
   ```
   cd docker_demo
   rm -rf venv
   sudo apt install python3.11-venv (press OK and space bar and Ok when prompted)
   python3.11 -m venv .venv
   python3 -m pip install --upgrade pip
   source .venv/bin/activate   
   terminal should have (.venv) prepended
   pip install -r requirements.txt
   flask run (Open Browser and Test)
   ```
## Confirm Docker setup
   ```
   docker build -t cbagade/py-first-prog:v1 .
   ```

## Install docker-compose
   find latest -version at - 

   https://github.com/docker/compose/releases
   ```
   sudo curl -L "https://github.com/docker/compose/releases/download/2.29.7/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   docker compose version
   ```

## To stop vagrnat machine
   vagrant halt

   always ensure to stop before shutting down your laptop

## To destroy machine
   vagrant destroy

## Git Steps

```
   Create a token :: Settings -> Developer Settings -> Personal Access Token -> Token classic -> Generate New token -> Give all permissions

   Save token to your local machine

   Github -> Create a private repo -> Copy URL

   On to you local machine, execute following instruction

   Sample URL - https://github.com/cbagade/classdemo.git

   git clone https://<user>:<token>@github.com/cbagade/classdemo.git

   cd <your repo>

   create some file

   git add <file>

   git commit -m "commit message"

   git push -u origin main
```
