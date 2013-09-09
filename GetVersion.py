#!/usr/bin/python 

from commands import getoutput
import os

def get_version():
    """Get version of the tool based on state of the git repository.
    required: git"""
    path = os.path.dirname(__file__)
    if os.path.islink(path + os.sep + os.path.basename(__file__)):
        path = os.path.dirname(os.readlink(path + os.sep + os.path.basename(__file__)))
    if not path: path = '.'
    curr_path = os.getcwd()
    os.chdir(path)
    version = ' ver:' + getoutput('git describe --long --tags --dirty --always')
    os.chdir(curr_path)
    return version

if __name__ == '__main__':
    print os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), get_version()