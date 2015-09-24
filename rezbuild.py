__author__ = 'jack.straw'
import os
import re
import pprint
import shutil
from collections import OrderedDict


bez_files = ['build.rxt', '.bez.yaml']


def build(source_path, build_path, install_path, targets):
    def rmrf(path):
        if os.path.isdir(path):
            map(rmrf, (os.path.join(path, n) for n in os.listdir(path)))
            os.remove(path)
        else:
            if os.path.basename(path) not in bez_files:
                os.unlink(path)

    map(rmrf, (os.path.join(build_path, n) for n in os.listdir(build_path)))

    # copy python module
    shutil.copy(os.path.join(source_path, 'pathlib2.py'), build_path)

    if targets and 'install' in targets:
        if os.path.exists(install_path):
            map(rmrf, (os.path.join(install_path, n) for n in os.listdir(install_path)))
        else:
            os.mkdir(install_path)
        print os.listdir(build_path)
        map(
            lambda p: shutil.copytree(os.path.join(build_path, p), os.path.join(install_path, p))
                        if os.path.isdir(os.path.join(build_path, p))
                        else shutil.copy(os.path.join(build_path, p), install_path),
            os.listdir(build_path)
        )
