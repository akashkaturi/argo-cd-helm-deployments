# Argocd Deployments

## Create Helm chart

```bash
helm create helloworld
```

## Start Minikube server

```bash
minikube start
```

(if not installed, install argocd)

## Kube Commands

```bash
#to get argocd services
kubectl get svc -n argocd 

#portforwarding to argocd-server to access the UI
kubectl port-forward svc/argocd-server -n argocd 8080:443   
```

## Login to argocd UI
```bash
# To get argocd UI password
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d

# install argocd
brew install argocd

# login to argocd
argocd login 127.0.0.1:8080  

# to update password
argocd account update-password --current-password curr_password --new-password new_password
```


