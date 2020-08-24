```
kubectl get jobs

kubectl get pods --selector=job-name=pi --output=jsonpath='{.items[*].metadata.name}'


kubectl get daemonset  --namespace=kube-system

kubectl edit  daemonset  kube-proxy   --namespace=kube-system


# status 

kubectl edit  deployment


kubectl api-versions|grep batch



kubectl get  replicaset  -A


DESIRED 期望数量  CURRENT 当前数量
 
 
 
Controlled by  Events
```
