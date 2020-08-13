## 准备数据库
```
source ./db/qmplus.sql


```

## 准备后端
go build 

```


```

## 准备前端

npm run build 

```
user nginx;
worker_processes  auto;

events {
    worker_connections  1024;
}

http {
    sendfile            on;
    tcp_nopush          on;
    tcp_nodelay         on;
    keepalive_timeout   65;
    types_hash_max_size 2048;
    include               /usr/local/nginx/conf/mime.types;
#    default_type        application/octet-stream;
server {
        listen       80;
        server_name default_server;
        root /var/www/html/resource/dist;
        index index.html index.htm;
 
        #charset koi8-r;
        #access_log  logs/host.access.log  main;
 
        location / {
        add_header Cache-Control 'no-store, no-cache, must-revalidate, proxy-                        
        revalidate, max-age=0';
        try_files $uri $uri/ /index.html;
                  }

        location  /v1 {
  		        proxy_set_header Host $http_host;
			proxy_set_header  X-Real-IP $remote_addr;
			proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
			proxy_set_header X-Forwarded-Proto $scheme;
    	                rewrite ^/v1/(.*)$ /$1 break;  #重写
    	                proxy_pass http://127.0.0.1:8888; # 设置代理服务器的协议和地址
                     }


        location /api/swagger/index.html {
                       proxy_pass http://127.0.0.1:8888/swagger/index.html;
                                         }


     }

}



```
