#!/usr/bin/python3
"""
Module 1-pack_web_static:
Fabric script that distributes an archive to your web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['52.91.132.67', '54.237.56.213']


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if exists(archive_path) is False:
        return False
    try:
        filename = archive_path.split("/")[-1]
        name = filename.split(".")[0]
        target_path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(target_path, name))
        run("tar -xzf /tmp/{} -C {}{}/".format(filename, target_path, name))
        run("rm /tmp/{}".format(filename))
        run("mv {0}{1}/web_static/* {0}{1}/".format(target_path, name))
        run("rm -rf {}{}/web_static".format(target_path, name))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(target_path, name))
        return True
    except:
        return False
