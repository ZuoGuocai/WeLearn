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
