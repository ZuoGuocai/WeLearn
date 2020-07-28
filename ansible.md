- ansible config

```
roles_path    = /opt/ansible_demo/roles
host_key_checking = False
callback_whitelist = profile_tasks

[ssh_connection]
pipelining = True
```


- hosts
```
[web_group]
#172.24.126.13
172.24.126.[2:254]

[web_group:vars]
ansible_ssh_user = root
ansible_ssh_port = 22 
ansible_ssh_pass = xxx
#ansible_ssh_private_key_file=/opt/ansible_demo/keys/openstack

```


-C  

-e 

ansible  -i hosts  web_group  -m ping

```



```



```



```



```


```
