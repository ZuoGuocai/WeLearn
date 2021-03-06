## kubectl 命令集
```
kubectl delete pods -l app=nginx -n default
kubectl get  pods -A |grep nginx
kubectl exec   nginx-deployment-cc7df4f8f-9j89m   -- printenv |grep SERVICE
kubectl get services kube-dns --namespace=kube-system
kubectl run curl --image=radial/busyboxplus:curl -i --tty 
kubectl logs  -f  nginx-deployment-674ff86d-ktnvq   -n default
kubectl get deployment  -n kube-system  --field-selector metadata.name=kuboard  -o yaml
```


## dns
zuoguocai.com   172.23.250.132

## haproxy
```
listen k8s-nodes
bind 172.23.250.132:80
server node01 172.24.126.114:80 check inter 2000 rise 2 fall 5
server node02 172.24.126.115:80 check inter 2000 rise 2 fall 5
listen k8s-nodes-tls
bind 172.23.250.132:443
server node01 172.24.126.114:443 check inter 2000 rise 2 fall 5
server node02 172.24.126.115:443 check inter 2000 rise 2 fall 5

```

## namespace
```
kubectl  create namespace  yunwei
```

## secret 

```
kubectl create secret tls nginx-ingress-tls-secret  --cert=zuoguocai.com.crt --key=zuoguocai.com.key  -n yunwei
```

## 本地存储 hostPath

```
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: showdoc
  name: showdoc
  namespace: yunwei
spec:
  replicas: 2
  selector:
    matchLabels:
      app: showdoc
  template:
    metadata:
      labels:
        app: showdoc
    spec:
      containers:
      - image: registry.cn-shenzhen.aliyuncs.com/star7th/showdoc:latest
        name: showdoc
        resources:
          requests:
            cpu: 0.5
            memory: 500Mi
          limits:
            cpu: 0.5
            memory: 500Mi
        ports:
          - name: http
            containerPort: 80
            protocol: TCP
        volumeMounts:
        - name: showdoc-data
          mountPath: /var/www/html
      volumes:
      - name: showdoc-data
        hostPath:
          path: /ccdata/k8s/data/showdoc

---
apiVersion: v1
kind: Service
metadata:
  name: showdoc
  namespace: yunwei
spec:
  ports:
  - name: http
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: showdoc
  type: NodePort

```


## 动态NFS
- showdoc-pvc.yaml
```
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: showdoc-claim
  namespace: yunwei
  annotations:
    volume.beta.kubernetes.io/storage-class: "nfs"
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 2G
```
- showdoc-deployment.yml
```
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: showdoc
  name: showdoc
  namespace: yunwei
spec:
  replicas: 3
  selector:
    matchLabels:
      app: showdoc
  template:
    metadata:
      labels:
        app: showdoc
    spec:
      containers:
      - image: registry.cn-shenzhen.aliyuncs.com/star7th/showdoc:latest
        name: showdoc
        resources:
          requests:
            cpu: 0.5
            memory: 500Mi
          limits:
            cpu: 0.5
            memory: 500Mi
        ports:
          - name: http
            containerPort: 80
            protocol: TCP
        volumeMounts:
        - name: showdoc-data
          mountPath: /var/www/html
      volumes:
      - name: showdoc-data
        persistentVolumeClaim:
          claimName: showdoc-claim
---
apiVersion: v1
kind: Service
metadata:
  name: showdoc
  namespace: yunwei
spec:
  ports:
  - name: http
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: showdoc
  type: NodePort

```
- cat  showdoc-ingress.yaml

```
apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  name: my-ingress-for-showdoc  # Ingress 的名字，仅用于标识
  namespace: yunwei
spec:
  tls:
  - hosts:
    - zuoguocai.com
    secretName: nginx-ingress-tls-secret
  rules:                      # Ingress 中定义 L7 路由规则
  - host: zuoguocai.com   # 根据 virtual hostname 进行路由（请使用您自己的域名）
    http:
      paths:                  # 按路径进行路由
      - path: /
        backend:
          serviceName: showdoc  # 指定后端的 Service 为之前创建的 nginx-service
          servicePort: 80

```
## troubshooting

```
kubectl logs -n yunwei $(kubectl get pod -n yunwei -l app=showdoc -o jsonpath='{.items[0].metadata.name}') -f
```
