```

k8s访问外部服务
k8s访问集群外的服务最好的方式是采用Endpoint方式(可以看作是将k8s集群之外的服务抽象为内部服务)，也可以直接使用外部服务的ip。

首先创建一个没有 selector的service，其不会创建相关的 Endpoints 对象


apiVersion: v1
kind: Service
metadata:
  name: mysql-test
spec:
  # 自定义暴露的Ip，可以不设置，直接用服务名称调用
  clusterIP: 10.106.96.101
  ports:
  - port: 3306
    targetPort: 3306
    protocol: TCP
​ 接着创建一个Endpoints，手动将 Service映射到指定的 Endpoints


apiVersion: v1
kind: Endpoints
metadata:
  # 名称必须和Service相同
  name: mysql-test
subsets:
  - addresses:
    # 多个ip可以再次列出
    - ip: 192.168.3.141
    - ip: 192.168.3.142
    ports:
    # 多个端口的话可以在此处列出，将上述两个ip的端口，映射到内部
    - port: 3306
      protocol: TCP
application.yml：服务使用service名称加端口访问

spring:
  application:
    name: dvis-sys-service
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    # 此处使用k8s的服务名称，或者使用自定义暴露的clusterIP
    url: jdbc:mysql://mysql-test:3306/local_mysql?useUnicode=true
    username: root
    password: root

```
