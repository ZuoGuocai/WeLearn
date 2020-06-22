clickhouse 快速上手

# 配置密码

```

vi /etc/clickhouse-server/users.xml


配置成明文
<password>qwerty</password>


PASSWORD=$(base64 < /dev/urandom | head -c8); echo "$PASSWORD"; echo -n "$PASSWORD" | sha1sum | tr -d '-' | xxd -r -p | sha1sum | tr -d '-'
配置成密文
<password_sha256_hex>65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5</password_sha256_hex>

systemctl restart clickhouse-server
```
# 基本查询

```

clickhouse-client -h 172.24.126.3   -d default -m -u default  --password xxx

CREATE TABLE test.csv (a String, b UInt64, c Int64, d String) ENGINE = Log;

insert into test.csv values('zuoguocai',1,1001,'male');

exit;

echo ',,,'|clickhouse-client -h 172.24.126.3   -d default -m -u default  --password xxx  --query="INSERT INTO test.csv FORMAT CSV"



```

#  clickhouse 代理 和  同步工具

```

https://github.com/Vertamedia/chproxy


https://github.com/long2ice/mysql2ch

```
