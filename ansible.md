- ansible config

```
forks         = 100
roles_path    = /opt/ansible_demo/roles  # 指定 roles 位置
host_key_checking = False           # 不检查 host key
callback_whitelist = profile_tasks  # 统计task执行时间插件

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

- 命令行参数

```
-C  check

-e  args

-vvv  verbose

ansible  -i hosts  web_group  -m ping
ansible  -i hosts  web_group    --list-hosts
ansible-playbook   -i hosts    playbook01.yml    -e  'my_host=web_group'
ansible-playbook   -i hosts   nginx.yml -C



```

- playbook + roles

```
mkdir nginx/{defaults,files,handlers,tasks,templates,meta}  -p


```


- 插件
```
profile_tasks


```


- 异步和并发
```


```

- 样例库

https://github.com/dl528888/ansible-examples

- 参考文件
https://www.cnblogs.com/yanjieli/p/10969299.html
https://www.ibm.com/developerworks/cn/linux/1608_lih_ansible/index.html
