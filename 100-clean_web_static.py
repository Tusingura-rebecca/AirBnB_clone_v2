#!/usr/bin/python3
"""
Module 1-pack_web_static:
Fabric script that distributes an archive to your web servers
"""

import os
from datetime import datetime as dt
from fabric.api import env, local, lcd, cd, run

env.user = 'ubuntu'
env.hosts = ['100.24.74.255', '52.86.146.141']
env.key_filename = ['~/.ssh/alx.key', '~/.ssh/alx']


def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number (int): The number of archives to keep.
        If number is 0 or 1, keeps only the most recent archive. If
        number is 2, keeps the most and second-most recent archives,
        etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
