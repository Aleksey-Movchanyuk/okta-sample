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

docker-compose -f docker-compose.yml build iap-database
docker-compose -f docker-compose.yml up -d --no-build iap-database
docker-compose -f docker-compose.yml stop iap-database

docker-compose -f docker-compose.yml build iap-backend
docker-compose -f docker-compose.yml up -d --no-build iap-backend
docker-compose -f docker-compose.yml stop iap-backend

docker-compose -f docker-compose.yml build iap-frontend
docker-compose -f docker-compose.yml up -d --no-build iap-frontend
docker-compose -f docker-compose.yml stop iap-frontend

docker exec -it iap_backend /bin/bash
docker exec --user="root" -it iap_backend /bin/bash

docker-compose -f docker-compose.yml run iap-backend /bin/bash
docker-compose -f docker-compose.yml run iap-frontend /bin/bash

docker-compose down --volumes

docker image ls --all
docker image prune -a --force

docker tag 56ef77140652 gcr.io/iap-frontend/iap-frontend:2.1.2.8
docker push gcr.io/gcp-project-abc/iap-frontend:2.1.2.8
```

Restart Docker daemon
```
killall Docker && open /Applications/Docker.app
```
