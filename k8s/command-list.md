```
kubectl get jobs

kubectl get pods --selector=job-name=pi --output=jsonpath='{.items[*].metadata.name}'


kubectl get daemonset  --namespace=kube-system

kubectl edit  daemonset  kube-proxy   --namespace=kube-system


# status 

kubectl edit  deployment


kubectl api-versions|grep batch
```
