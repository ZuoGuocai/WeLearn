```
kubectl get pods --selector=job-name=pi --output=jsonpath='{.items[*].metadata.name}'




```
