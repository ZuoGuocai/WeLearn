grafana html-----------nginx header------------- kibana for aws (opendistroforelasticsearch-kibana)

# kibana 

opendistro_security

tag cloud 

分享

# nginx 代理认证
---

```

server {
        listen 443 ssl;
        server_name kibana7.xxx.com;
        ssl_certificate  xxx.com.crt;
        ssl_certificate_key  xxx.com.key;
        ssl_session_timeout  5m;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;     #指定SSL服务器端支持的协议版本
        ssl_ciphers  HIGH:!aNULL:!MD5;
        #ssl_ciphers  ALL：!ADH：!EXPORT56：RC4+RSA：+HIGH：+MEDIUM：+LOW：+SSLv2：+EXP;    #指定加密算法
        ssl_prefer_server_ciphers   on;    #在使用SSLv3和TLS协议时指定服务器的加密算法要优先于客户端的加密算法

    location / {
        proxy_pass   http://kibana_backend/;
        proxy_set_header  Host $host;
        proxy_set_header  X-Real-IP $remote_addr;
        proxy_set_header  X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header  Authorization "Basic YWRtaW46Vmlwa2lkQEVsaw==";
    }

}




```



# grafana html  iframe 



```
<iframe src="https://kibana7.xxx.com/app/kibana#/visualize/edit/14da2260-a700-11ea-93ba-a9a125fcf025?embed=true&_g=()" height="900" width="1200" style="POSITION:absolute;RIGHT:500px; LEFT:-50px; TOP:-100px;"></iframe>

```


```
<iframe id="inlineFrameExample"
    title="Inline Frame Example"
    width="1200"
    height="900"
    src="https://map.baidu.com">
</iframe>

```
