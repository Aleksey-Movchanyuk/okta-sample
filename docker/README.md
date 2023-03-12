### Docker post install
1. Create docker's virtual machine if not exists
```
docker-machine ls
docker-machine create -d virtualbox default
docker-machine ls

docker-machine env default
eval $(docker-machine env default)
env | grep DOCKER

docker-machine start default
docker-machine ip default
```
#### Port Forwarding
A Docker Machine is a virtual machine running under VirtualBox in your host machine. We can use the Port Forwarding feature of VirtualBox in order to access the Docker VM as localhost.

To achieve this do the following:

First of all, make sure your Docker Machine is stopped by executing the following:
```
docker-machine stop tableau-reporter.local
```
Then:
* Open VirtualBox Manager
* Select your Docker Machine VirtualBox image (e.g.: default)
* Open Settings -> Network -> Advanced -> Port Forwarding
* Add your app name, the desired host port and your guest port

Now you are ready to start your Docker Machine by executing the following:
```
docker-machine start default
eval $(docker-machine env default)
```

Then just start your Docker container and you will be able to access it via localhost.

#### Docker useful commands
```
docker-compose -f docker-compose.yml up -d --build
docker-compose -f docker-compose.yml up -d --no-build
docker-compose -f docker-compose.yml down

docker-compose -f docker-compose.yml build okta-sample-linux
docker-compose -f docker-compose.yml up -d --no-build okta-sample-linux
docker-compose -f docker-compose.yml stop okta-sample-linux

docker-compose -f docker-compose.yml build okta-sample-linux
docker-compose -f docker-compose.yml up -d --no-build okta-sample-linux
docker-compose -f docker-compose.yml stop okta-sample-linux

docker exec -it okta-sample-linux /bin/bash
docker exec --user="root" -it okta-sample-linux /bin/bash

docker-compose -f docker-compose.yml run okta-sample-linux /bin/bash

docker-compose down --volumes

docker image ls --all
docker image prune -a --force

https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication?tabs=azure-cli#admin-account
docker login oktasampleregistry.azurecr.io

docker tag 39ac8d6b5e36 oktasampleregistry.azurecr.io/okta-sample-linux:v1.0
docker push oktasampleregistry.azurecr.io/okta-sample-linux:v1.0
```

Restart Docker daemon
```
killall Docker && open /Applications/Docker.app
```
