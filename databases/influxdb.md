# influxdb

```
create user "admin" with password 'admin' with all privileges;
influx -username 'admin' -password 'admin@123';
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

# grafana variables

```

ip	show tag values from hosts with key="ip" where uuid=~ /$uuid/				
hostname	show tag values from hosts with key="instance" where uuid=~ /$uuid/			


```
