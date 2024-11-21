## Deploying the weather-app on AWS-EKS cluster using argo-cd ##

1- Create a ec2 instance of t2.medium and git clone the project

   Install docker for creating the image of the application with cmd 
   
> sudo apt-install docker.io -y
 
> sudo chown $USER /var/run/docker.sock
   

2- Now, to push the image to the AWS -ECR we need to install aws cli. If not ECR , you can even push the image to docker hub.

You can install aws cli with the following cmds :  
  
> curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

> sudo apt install unzip

> unzip awscliv2.zip

> sudo ./aws/install -i /usr/local/aws-cli -b /usr/local/bin --update

3 - Then create a user in your aws account and generate access keys token , run aws configure cmd and put these keys.

   Create a ecr registery in your aws account, and apply the image push cmds provided by aws.
    
   Now, your image is safely pushed to the AWS ECR. 

4 - Install kubectl and ekctl with following cmds:

> insatlling kubectl:

  > curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.19.6/2021-01-05/bin/linux/amd64/kubect

   > chmod +x ./kubectl
 
  > sudo mv ./kubectl /usr/local/bin
 
   > kubectl version --short --client

> installing ekctl :

> curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
 
   > sudo mv /tmp/eksctl /usr/local/bin
 
   > eksctl version


  5 - create the eks cluster with the cmd - 
  
   > eksctl create cluster --name weather-app --region ap-south-1 --node-type t2.medium --nodes-min 2 --nodes-max 2

  6 - Install argo cd-
  
   > kubectl create namespace argocd
 
> kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

> check for argocd pods-

> kubectl get pods -n argocd and when everything is running run the following cmd : 

  > "kubectl port-forward svc/argocd-server -n argocd 8080:443 --address=0.0.0.0 &"   (enable port 8080 in your security group of the instance)
 
 > deafult username of argocd is "admin" and to get the password, perform following steps

 > kubectl get secret -n argocd
 
 > kubectl edit secret argocd-initial-admin-secret -n argocd
 
 > echo <your-cryptographic-code> | base64 --decode

 > paste this paswd and you can now access argocd



7- In the deployment file give the image of the application , which is present in your aws-ecr

8 - Select new app , and complete the form by 
  
   > giving application name (in small letters) and project name: deafult, sync policy: automatic, tick prune resources and self-heal
      
   > sync options: tick auto-create namespace and apply out of sync only
      
   > giving github url and under revision section give the github branch in which code is present , which is master 
      
   > set path as . , as the manifest files are present in root directoy
      
   > Give cluster url , which is auto-created and give namespace "deafult"
      
   > Then create the app
      
   > To access the app on browser run - "kubectl port-forward svc/weather-app-service 5000:5000 --address 0.0.0.0 &" (enable port 5000 in your security group of your instance)
> 



 ![image alt](https://github.com/kadamvignesh/weather-app/blob/master/Screenshot%20(93).png?raw=true)
 



      



    



   
