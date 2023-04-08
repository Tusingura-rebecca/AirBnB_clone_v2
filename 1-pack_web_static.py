#!/usr/bin/python3
"""Module 1-pack_web_static: Fabric script that generates a .tgz archive"""

from fabric.api import local
from datetime import datetime as dt
from os.path import isdir


def do_pack():
    """generates a .tgz archive"""
    try:
        if isdir("versions") is False:
            local("mkdir versions")
        filename = "versions/web_static_{:%Y%m%d%H%M%S}.tgz".format(dt.now())
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except:
        return None
