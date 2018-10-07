# -*- coding: utf-8 -*-
# @Time    : 2018/9/9 11:22 PM
# @Author  : Zhixin Piao 
# @Email   : piaozhx@shanghaitech.edu.cn

import sys

sys.path.append('./')

import os
from db.db_manager import DatabaseManager


def create_container_on_remote(node_name, docker_type, container_name, cname, shm_size, container_port, add_open_port_str):


    os.system("ssh %s "
              "%s run "
              "--name %s "
              "-v /home/%s:/home/%s "
              "-v /p300/datasets:/datasets:ro "
              "-v /p300/docker/%s/bin:/bin "
              "-v /p300/docker/%s/etc:/etc "
              "-v /p300/docker/%s/lib:/lib "
              "-v /p300/docker/%s/lib64:/lib64 "
              "-v /p300/docker/%s/opt:/opt "
              "-v /p300/docker/%s/root:/root "
              "-v /p300/docker/%s/sbin:/sbin "
              "-v /p300/docker/%s/usr:/usr "
              "--privileged=true "
              # "--volume /run/dbus/system_bus_socket:/run/dbus/system_bus_socket:ro "
              "--restart unless-stopped "
              "--add-host node01:10.10.10.101 "
              "--add-host node02:10.10.10.102 "
              "--add-host node03:10.10.10.103 "
              "--add-host node04:10.10.10.104 "
              "--add-host node05:10.10.10.105 "
              "--add-host node06:10.10.10.106 "
              "--add-host node07:10.10.10.107 "
              "--add-host node08:10.10.10.108 "
              "--add-host node09:10.10.10.109 "
              "--add-host node10:10.10.10.110 "
              "--add-host node11:10.10.10.111 "
              "--add-host node12:10.10.10.112 "
              "--add-host node13:10.10.10.113 "
              "--add-host node14:10.10.10.114 "
              "--add-host node15:10.10.10.115 "
              "--add-host node16:10.10.10.116 "
              "--add-host node17:10.10.10.117 "
              "--add-host node18:10.10.10.118 "
              "--add-host node19:10.10.10.119 "
              "--add-host node20:10.10.10.120 "
              "--add-host node21:10.10.10.121 "
              "--add-host node22:10.10.10.122 "
              "--add-host node23:10.10.10.123 "
              "--add-host node24:10.10.10.124 "
              "--add-host node25:10.10.10.125 "
              "--add-host node26:10.10.10.126 "
              "--add-host admin:10.10.10.100 "
              "--shm-size=%s "
              "-h %s "
              "-d "
              "-p %d:22 "
              "%s "
              "deepo_plus "
              "/usr/sbin/sshd -D" % (
                  node_name, docker_type, container_name, cname, cname, cname, cname, cname, cname, cname, cname, cname, cname, shm_size,
                  container_name, container_port, add_open_port_str))

    print("create container on %s successful!" % node_name)


def rm_container_on_remote(node_name, container_name):
    os.system('ssh %s "docker stop %s && docker rm %s"' % (node_name, container_name, container_name))
    print('close', container_name, 'done')


def main():
    db = DatabaseManager()
    user_info_list = db.get_all_user_info()

    for user_info in user_info_list:
        username = user_info['username']
        cname = username
        container_port = user_info['container_port']
        open_port_range = user_info['open_port_range']

        if username not in ['yanshp']:
            continue

        for permission_detail in user_info['permission']:
            node_name = permission_detail['name']
            docker_type = 'docker' if node_name == 'admin' else 'nvidia-docker'

            container_name = '%s.%s' % (username, node_name)

            add_open_port_str = "-p %s:%s" % (open_port_range, open_port_range) if node_name == 'admin' else ''

            memory_size = os.popen('''ssh %s  free -h | head -n 2 | tail -n 1 | awk -F' ' '{print $2}' ''' % node_name).read().strip()
            memory_unit = memory_size[-1]
            memory_size = int(memory_size[:-1])
            shm_size = memory_size // 2
            shm_size = str(shm_size) + memory_unit

            rm_container_on_remote(node_name, container_name)
            create_container_on_remote(node_name, docker_type, container_name, cname, shm_size, container_port, add_open_port_str)

            print("create container %s successfully." % container_name)



if __name__ == '__main__':
    main()
