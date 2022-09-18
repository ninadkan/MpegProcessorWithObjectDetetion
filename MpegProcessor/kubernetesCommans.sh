# Commands on Kubernetes to work
kubectl create -f ./first-app/pod-helloworld.yml

# useful kubernetes Commands
kubectl get pod  
kubectl describe pos <poc>
kubectl expose pod <> pod --port=444 --name=frontend # expose a port of a pod (creates a new service)
kubectl port-forward <pod> 8080  # port forward the exposed pod port to your local machine
kubectl attach <podname> -i  # attach to the pod
kubectl exec <pod> --Commands # runs on first container else need to specify container
kubectl label pods <pod> mylabe=awesome  # add a new label to a pod
kucectl run -i --tty busybox --image=busybox --restart=Never -- sh # usefule for debugging


#runing example

(.venv) azureuser@NinadK-MPEG-Parser:~/kubernetes-course/first-app$ kops validate cluster
Your cluster training.ninadkanthi.co.uk is ready
(.venv) azureuser@NinadK-MPEG-Parser:~/kubernetes-course/first-app$ ls
helloworld-nodeport-service.yml  helloworld-service.yml  helloworld.yml
(.venv) azureuser@NinadK-MPEG-Parser:~/kubernetes-course/first-app$ cat helloworld.yml 
apiVersion: v1
kind: Pod
metadata:
  name: nodehelloworld.example.com
  labels:
    app: helloworld
spec:
  containers:
  - name: k8s-demo
    image: ninadkanthi/k8s-demos
    ports:
    - name: nodejs-port
      containerPort: 3000
(.venv) azureuser@NinadK-MPEG-Parser:~/kubernetes-course/first-app$ kubectl create -f helloworld.yml 
pod/nodehelloworld.example.com created
(.venv) azureuser@NinadK-MPEG-Parser:~/kubernetes-course/first-app$ kubectl get pod
# after some time 
NAME                         READY   STATUS    RESTARTS   AGE
nodehelloworld.example.com   1/1     Running   0          2m38s
(.venv) azureuser@NinadK-MPEG-Parser:~/kubernetes-course/first-app$ kubectl describe pod nodehelloworld.example.com
Name:         nodehelloworld.example.com
Namespace:    default
...

(.venv) azureuser@NinadK-MPEG-Parser:~/kubernetes-course/first-app$ kubectl port-forward nodehelloworld.example.com 8081:3000
Forwarding from 127.0.0.1:8081 -> 3000
Forwarding from [::1]:8081 -> 3000
Handling connection for 8081
Handling connection for 8081
CTRL+C to come out


(.venv) azureuser@NinadK-MPEG-Parser:~/kubernetes-course/first-app$ kubectl expose pod nodehelloworld.example.com --type=NodePort --name nodehelloword-service
service/nodehelloword-service exposed
(.venv) azureuser@NinadK-MPEG-Parser:~/kubernetes-course/first-app$ kubectl get service
NAME                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
kubernetes              ClusterIP   100.64.0.1      <none>        443/TCP          50m
nodehelloword-service   NodePort    100.65.54.127   <none>        3000:32303/TCP   13s
(.venv) azureuser@NinadK-MPEG-Parser:~/kubernetes-course/first-app$ 


# More commands 
(.venv) azureuser@NinadK-MPEG-Parser:~/kubernetes-course/first-app$ kubectl attach nodehelloworld.example.com
If you don't see a command prompt, try pressing enter.


# because our process is not outputting anything we don't see anything here. 
# CTRL-C to come out

(.venv) azureuser@NinadK-MPEG-Parser:~/kubernetes-course/first-app$ kubectl exec nodehelloworld.example.com -- ls /app
Dockerfile
README.md
docker-compose.yml
index-db.js
index.js
misc
node_modules
package-lock.json
package.json
package.json.original
test


(.venv) azureuser@NinadK-MPEG-Parser:~/kubernetes-course/first-app$ kubectl get service
NAME                    TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
kubernetes              ClusterIP   100.64.0.1      <none>        443/TCP          58m
nodehelloword-service   NodePort    100.65.54.127   <none>        3000:32303/TCP   8m27s
(.venv) azureuser@NinadK-MPEG-Parser:~/kubernetes-course/first-app$ kubectl describe nodehelloword-service
error: the server doesnt have a resource type "nodehelloword-service"

(.venv) azureuser@NinadK-MPEG-Parser:~/kubernetes-course/first-app$ kubectl describe service nodehelloword-service
Name:                     nodehelloword-service
Namespace:                default
Labels:                   app=helloworld
Annotations:              <none>
Selector:                 app=helloworld
Type:                     NodePort
IP Family Policy:         SingleStack
IP Families:              IPv4
IP:                       100.65.54.127
IPs:                      100.65.54.127
Port:                     <unset>  3000/TCP
TargetPort:               3000/TCP
NodePort:                 <unset>  32303/TCP
Endpoints:                100.96.1.6:3000
Session Affinity:         None
External Traffic Policy:  Cluster
Events:                   <none>

# starting another busybox container on our pod
(.venv) azureuser@NinadK-MPEG-Parser:~/kubernetes-course/first-app$ kubectl run -i --tty busybox --image=busybox --restart=Never
If you dont see a command prompt, try pressing enter.
/ # ls
bin   dev   etc   home  proc  root  sys   tmp   usr   var
/ # 
/ # ls
bin   dev   etc   home  proc  root  sys   tmp   usr   var
/ # 
/ # telnet 100.96.1.6:3000
Connected to 100.96.1.6:3000

GET /

HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: text/html; charset=utf-8
Content-Length: 12
ETag: W/"c-Lve95gjOVATpfV8EL5X4nxwjKHE"
Date: Sun, 18 Sep 2022 16:42:23 GMT
Connection: close

Hello World!Connection closed by foreign host
/ # 


(.venv) azureuser@NinadK-MPEG-Parser:~/kubernetes-course/first-app$ cat helloworld-service.yml 
apiVersion: v1
kind: Service
metadata:
  name: helloworld-service
spec:
  ports:
  - port: 80
    targetPort: nodejs-port
    protocol: TCP
  selector:
    app: helloworld
  type: LoadBalancer
(.venv) azureuser@NinadK-MPEG-Parser:~/kubernetes-course/first-app$ 


(.venv) azureuser@NinadK-MPEG-Parser:~/kubernetes-course/first-app$ code helloworld.yml 
(.venv) azureuser@NinadK-MPEG-Parser:~/kubernetes-course/first-app$ kubectl create -f helloworld.yml 
Error from server (AlreadyExists): error when creating "helloworld.yml": pods "nodehelloworld.example.com" already exists
(.venv) azureuser@NinadK-MPEG-Parser:~/kubernetes-course/first-app$ kubectl create -f helloworld-service.yml 
service/helloworld-service created

# now check the load balancer running on the AWS. 
# and using the load balancer URL, you can put the whole thing to working
# http://a41ff8772ede2447b952a03ddaa739f6-1269578866.eu-west-2.elb.amazonaws.com/ 


kubectl exec -it <nodename> --bash
kubectl logs <nodename>