
```
kubeclt   create namespace  yunwei
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


