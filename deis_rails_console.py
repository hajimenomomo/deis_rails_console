#!/usr/local/bin/python

"""
This script is to be put in a deis app directory or in your PATH and allows you to open an interactive rails console
directly related to your app, it requires slightly customizing your Deis cluster by opening the Docker Remote API with
TLS encryption, and putting your client certificates in ~/.docker directory, as you would normally, the deis client is
also required
"""

import subprocess
import docker
import dockerpty
from os import path
__author__ = 'Mohamed Messaad'


def get_hosts_list(filename):
    hosts_list = []
    with open(filename) as f:
        for line in f:
            line = line.rstrip('\n')
            hosts_list.append(line)
    return hosts_list


def get_web_containers(docker_host):
    web_containers_list = []
    for container in docker_host.containers():
        if out.split()[1] in container['Names'][0] and 'web' in container['Command']:
            web_containers_list.append(container)
    return web_containers_list


if __name__ == '__main__':
    p = subprocess.Popen(['deis', 'ps'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()

    if len(out) == 0:
        print 'Deis client not installed or no apps associated to current path'
        print err
        exit(-1)

    tls_config = docker.tls.TLSConfig(
        client_cert=(path.expanduser('~/.docker/cert.pem'), path.expanduser('~/.docker/key.pem')),
        verify=path.expanduser('~/.docker/ca.pem'))

    cluster = []
    for host_url in get_hosts_list(path.expanduser('~/.docker/deis_hosts')):
        print 'https://{}:2376'.format(host_url)
        cluster.append(docker.Client(base_url='https://{}:2376'.format(host_url), tls=tls_config, version='auto'))

    target_container = None

    for host in cluster:
        web_containers = get_web_containers(host)
        if len(web_containers) != 0:
            target_container = web_containers[0]
            target_host = host
            break

    if target_container is not None:
        rails_console_container = target_host.create_container(
                    image=target_container['Image'],
                    stdin_open=True,
                    tty=True,
                    command='rails c',
                )
        dockerpty.start(target_host, rails_console_container)
