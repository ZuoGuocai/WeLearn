```
FROM node:12.16.1 as gva-web

WORKDIR /gva_web/
COPY web/ .

RUN cat .env.production
COPY docker/web-handle.sh .
RUN sh ./web-handle.sh
RUN cat .env.production
RUN rm -f web-handle.sh

RUN npm install -g cnpm --registry=https://registry.npm.taobao.org
RUN cnpm install || npm install
RUN npm run build

FROM golang:alpine as gva-server

ENV GO111MODULE=on
ENV GOPROXY=https://goproxy.io,direct
WORKDIR /go/src/gin-vue-admin
COPY server/ ./

RUN cat ./core/server.go
RUN cat ./config.yaml
COPY docker/server-handle.sh .
RUN sh ./server-handle.sh
RUN rm -f server-handle.sh
RUN cat ./core/server.go
RUN cat ./config.yaml

RUN go env && go list && go build -o gva-server .


FROM nginx:alpine
LABEL MAINTAINER="SliverHorn"

WORKDIR gva/

# copy web
COPY --from=gva-web /gva_web/dist ./resource/dist
# copy server
COPY --from=gva-server /go/src/gin-vue-admin/gva-server ./
COPY --from=gva-server /go/src/gin-vue-admin/config.yaml ./
COPY --from=gva-server /go/src/gin-vue-admin/resource ./resource


EXPOSE 8888

ENTRYPOINT ./gva-server

# 根据Dockerfile生成Docker镜像

# docker build -t gva-server:1.0 .

#- 根据Docker镜像启动Docker容器
#    - 后台运行
#    - ```
#    docker run -d -p 8888:8888 --name gva-server-v1 gva-server:1.0
#      ```
#    - 以可交互模式运行, Ctrl + p + q
#    - ```
#    docker run -it -p 8888:8888 --name gva-server-v1 gva-server:1.0
#      ```
```


# 常用

```
docker-compose up

docker-compose up --build

docker-compose up -d

 docker ps --no-trunc
```
# docker 网络冲突解决


- docker0 网络冲突

vi /etc/docker/daemon.yaml

{
    "bip":"192.168.0.1/24"
}

{
  "bip": "192.168.1.5/24",
  "fixed-cidr": "192.168.1.5/25",
  "fixed-cidr-v6": "2001:db8::/64",
  "mtu": 1500,
  "default-gateway": "10.20.1.1",
  "default-gateway-v6": "2001:db8:abcd::89",
  "dns": ["10.20.1.2","10.20.1.3"]
}


- docker-compose 桥接网络冲突

```
docker network create -d bridge --subnet=192.168.1.0/24 --gateway=192.168.1.254 test


docker-compose.yaml

networks:
  default:
    external:
      name: test

```
http://www.xiaomaidong.com/?p=1336

- docker swarm  网络冲突

```
#docker network create -d overlay --subnet=192.168.0.0/24 --attachable myOverlay
在不同的hosts(M, W1 与 W2)上面新建立containers,（busybox1, busybox2 和 busybox3）


## run busybox1 on manage node
# docker run -itd --name=busybox1 --network=myOverlay busybox /bin/sh

https://www.cnblogs.com/atuotuo/p/7250695.html
```
