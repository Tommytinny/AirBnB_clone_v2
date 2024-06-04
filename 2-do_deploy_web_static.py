#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers
"""
from fabric.api import *
from os.path import exists
env.hosts = ['100.26.153.245', '100.26.162.10']


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        file_no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        sudo("mkdir -p {}{}/".format(path, file_no_ext))
        sudo("tar -xzf /tmp/{} -C {}{}/".format(file_name, path, file_no_ext))
        sudo("rm /tmp/{}".format(file_name))
        sudo("mv {0}{1}/web_static/* {0}{1}/".format(path, file_no_ext))
        sudo("rm -rf {}{}/web_static".format(path, file_no_ext))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {}{}/ /data/web_static/current".format(path, file_no_ext))
        print("New version deployed!")
        return True
    except Exception as e:
        return False
