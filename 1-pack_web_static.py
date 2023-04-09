#!/usr/bin/python3
"""Module 1-pack_web_static: Fabric script that generates a .tgz archive"""

from fabric.api import local
from datetime import datetime as dt
from os import path


def do_pack():
    """generates a .tgz archive"""
    file = "versions/web_static_{:%Y%m%d%H%M%S}.tgz".format(dt.now())
    if path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
