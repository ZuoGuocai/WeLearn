
collectd-------> influxdb ---------> grafana

---

# collectd 

```

vi /etc/collectd.conf
LoadPlugin network
<Plugin network>
   server "172.x.x.x" "25826"
</Plugin>



```


# influxdb install 

```
wget https://dl.influxdata.com/influxdb/releases/influxdb-1.8.0.x86_64.rpm

udo yum localinstall influxdb-1.8.0.x86_64.rpm

wget -P /usr/local/share/collectd https://raw.githubusercontent.com/collectd/collectd/master/src/types.db

vi /etc/influxdb/influxdb.conf

[http]
  auth-enabled = true

[[collectd]]
  enabled = true
  bind-address = ":25826"
  database = "collectdb"
  retention-policy = ""
  typesdb = "/usr/local/share/collectd/types.db"
  batch-size = 5000
  batch-pending = 10
  batch-timeout = "10s"
  read-buffer = 0

```




# influxdb

```
create user "admin" with password 'admin' with all privileges;
influx -username 'admin' -password 'admin';
use collectdb;
show measurements;
show field keys;
DROP SERIES FROM 'measurement_name'
drop  measurement  hosts；

CREATE RETENTION POLICY "delete policy" ON "collectdb" DURATION 720h REPLICATION 1 DEFAULT;
SHOW RETENTION POLICIES ON collectdb;

show tag values from hosts with key="host" where availability_zone =~ /m1.tiny/

```





# influxdb api

```
#!/usr/bin/env bash
# author: zuoguocai@126.com


tmp_file="/tmp/.map.tmp"

# openstack 获取数据
source /root/scripts/admin-openrc.sh
openstack server list --all --long -f value 2>&1 > ${tmp_file}



# influxdb 清除数据
curl  'http://xxxx:8086/query' -u admin:admin --data-urlencode "db=collectdb" --data-urlencode "q=DROP MEASUREMENT hosts;"


# influxdb 写入数据
while read line
do
        host=`echo ${line} |awk '{print $10}'`
        instance_name=`echo ${line} |awk '{print $2}'`
        uuid=`echo ${line}  |awk '{print $1}'`
        ipaddress=`echo ${line} |awk '{print $6}'|awk -F'='  '{print $2}'`

        run="curl -s -connect-timeout 5 –XPOST \"http://xxxx:8086/write?db=collectdb&u=admin&p=admin\" --data-binary \"hosts,instance=${instance_name},ip=${ipaddress},host=${host},uuid=${uuid} value=1\""
        eval ${run}  

done<  ${tmp_file}


```
# influxdb backup and restore


```
#!/usr/bin/env bash
# author: zuoguocai@126.com
# influxdb backup and restore

influxd  backup  -database   collectdb     /tmp/backup

cd /tmp/backup
influxd restore -metadir /var/lib/influxdb/meta ./
influxd restore -database collectdb -datadir /var/lib/influxdb/data ./



```






# grafana variables

```

ip	show tag values from hosts with key="ip" where uuid=~ /$uuid/				
hostname	show tag values from hosts with key="instance" where uuid=~ /$uuid/			


```
