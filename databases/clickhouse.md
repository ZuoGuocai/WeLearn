# 配置密码

```

vi /etc/clickhouse-server/users.xml

systemctl restart clickhouse-server

clickhouse-client -h 172.24.126.3   -d default -m -u default  --password admin

CREATE TABLE test.csv (a String, b UInt64, c Int64, d String) ENGINE = Log;

insert into test.csv values('zuoguocai',1,1001,'male');

exit;

echo ',,,'|clickhouse-client -h 172.24.126.3   -d default -m -u default  --password admin  --query="INSERT INTO test.csv FORMAT CSV"



```
