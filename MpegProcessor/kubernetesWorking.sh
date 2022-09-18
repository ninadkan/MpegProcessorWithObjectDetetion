# installing for getting the Kubernetes cluster to work
# Getting the option 2
sudo apt-get update
sudo apt-get install -y ca-certificates curl
sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
sudo apt-get install -y kubectl
# to get the kubectl to work, fire the following command
kubectl cluster-info




# install Kops  
curl -Lo kops https://github.com/kubernetes/kops/releases/download/$(curl -s https://api.github.com/repos/kubernetes/kops/releases/latest | grep tag_name | cut -d '"' -f 4)/kops-linux-amd64
chmod +x kops
sudo mv kops /usr/local/bin/kops

# check that the installation works
kops

# Add the AWS security ID and code into our in_env_vard
code ./init_env_vars.sh 

# install the awsci
sudo apt install awscli
# add the secret-id and secret-code 
aws configure
# test that you see two folders as a result of following execution
# configure and ...
ls -al ~/.aws/
# if needed, this was needed in my case
sudo apt install bind9-host
# Test that your name resolution is working correctly
# It should return the host file from AWS
host -t NS training.ninadkanthi.co.uk

# create the ssh-keygen keys
ssh-keygen -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub 

# Getting the option of challenges that will work
kops create cluster --name=training.ninadkanthi.co.uk --state=s3@//ninadk-kops-bucket --zones=eu-west-2a --node-count=2 --node-size=t3.micro --master-size=t3.micro --dns-zone=training.ninadkanthi.co.uk --cloud=aws


# check if everything is working ok
kops validate cluster --state=s3://ninadk-kops-bucket

# if not best to delete and restart
kops delete  cluster --state=s3://ninadk-kops-bucket --yes


# for some reason the above was not working so tried the approach suggested in the trainign
sudo apt remove  kops
sudo apt remove  kubectl
cd MpegProcessorWithObjectDetetion/MpegProcessor/
source ./.venv/bin/activate
pip freeze > requirements.txt 
cat requirements.txt 
kubectl
whereis kops

# get cops
curl -Lo kops https://github.com/kubernetes/kops/releases/download/$(curl -s https://api.github.com/repos/kubernetes/kops/releases/latest | grep tag_name | cut -d '"' -f 4)/kops-linux-amd64
chmod +x kops
sudo mv kops /usr/local/bin/kops
kops
pip install awscli
#test that your domain is accessing
host -t NS training.ninadkanthi.co.uk

#install Kubectl
wget https://storage.googleapis.com/kubernetes-release/release/v1.24.5/bin/linux/amd64/kubectl
sudo mv kubectl /usr/local/bin/
sudo chmod +x /usr/local/bin/kubectl 
kubectl

# try starting the cluster again
kops create cluster --name=training.ninadkanthi.co.uk --state=s3://ninadk-kops-bucket --zones=eu-west-2a --node-count=2 --node-size=t3.micro --master-size=t3.micro --dns-zone=training.ninadkanthi.co.uk --cloud=aws
kops update cluster --name training.ninadkanthi.co.uk --yes --state=s3://ninadk-kops-bucket --admin

# you might require to install add-ons* possibly
# Suggestions:
# * validate cluster: kops validate cluster --wait 10m
# * list nodes: kubectl get nodes --show-labels
# * ssh to the master: ssh -i ~/.ssh/id_rsa ubuntu@api.training.ninadkanthi.co.uk
# * the ubuntu user is specific to Ubuntu. If not using Ubuntu please use the appropriate user based on your OS.
# * read about installing addons at: https://kops.sigs.k8s.io/addons


# ISSUE
(.venv) azureuser@NinadK-MPEG-Parser:~/MpegProcessorWithObjectDetetion/MpegProcessor$ kubectl version
Client Version: version.Info{Major:"1", Minor:"4", GitVersion:"v1.4.3", GitCommit:"4957b090e9a4f6a68b4a40375408fdc74a212260", GitTreeState:"clean", BuildDate:"2016-10-16T06:36:33Z", GoVersion:"go1.6.3", Compiler:"gc", Platform:"linux/amd64"}
Server Version: version.Info{Major:"1", Minor:"24", GitVersion:"v1.24.5", GitCommit:"e979822c185a14537054f15808a118d7fcce1d6e", GitTreeState:"clean", BuildDate:"2022-09-14T16:35:41Z", GoVersion:"go1.18.6", Compiler:"gc", Platform:"linux/amd64"}
(.venv) azureuser@NinadK-MPEG-Parser:~/MpegProcessorWithObjectDetetion/MpegProcessor$ kops version
Client version: 1.24.3 (git-v1.24.3)


# lets try to pass our public key as well
kops create cluster --name=$NAME --zones=eu-west-2a --master-size=t3.small --node-size=t3.small --node-count=2 --cloud aws --ssh-public-key="~/.ssh/id_rsa.pub"

# THIS FRIGGIN WORKS!!!!!!!!. need to deply to medium and not to the small. brilliant. 
# if you want only want one node, use th following

kops create cluster --name=$NAME --zones=eu-west-2a --master-size=t3.small --cloud aws --ssh-public-key="~/.ssh/id_rsa.pub"



