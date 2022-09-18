#! /bin/bash
# installing docker on ubuntu

# uninstall old versions
sudo apt-get remove docker docker-engine docker.io containerd runc

# setup the repository
sudo apt update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Add official Docker GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# use the following command to setup the repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# install the Docker engine
sudo apt update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Verify that Docker engine is installed correctly 
sudo service docker start
sudo docker run hello-world


# or apparently you can ge the latest 
sudo apt-get install docker.io  # I didn't test this one. 

# push an image to Docker hub
docker login
# first tag an already built image with your tag
docker tag imageid your-login/docker-demo 
# now move it to the cloud
docker push your-login/docker-demo


# or immediately tag an image during the build process
docker build -t your-login/docker-demo
# e,g, docker build -t ninadkanthi/k8s-demos .docker 
docker push your-login/docker-demo 


#making sure that the logged in user has all the permissions to use docker
sudo usermod -G docker azureuser

# Remarks
# you should run only one process in container
# all the data in the data is not preserved- you volumes. 
# 12factor.net is what you should 

# Next running the containers on 
# Remove all containers which either were created or have exited
docker rm $(docker ps -a -f status=exited -f status=created -q)

# docker remove all images
docker rmi $(docker images -a -q)

# to foecebly remove all images 
docker rmi -f $(docker images -a -q)

# finding out all the containers that are running
docker ps -a

# stopping a containers
docker stop <sontainerid>