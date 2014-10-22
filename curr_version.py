#!/usr/bin/python 
import os
import sh

def get_version(currfn='', verbose=False):
    """Get version of the tool based on state of the git repository.
    Return version. 

    If currfn is empty, then the path is '.'. Hmm.. I think it will work. We will see.

    The version is not printed!"""
    if currfn == '':
        path = '.'
    else:
        path = os.path.dirname(currfn)
    if verbose: print 'get_version::path', path
    if os.path.islink(currfn):#path + os.sep + os.path.basename(__file__)):
        path = os.path.dirname(os.readlink(path + os.sep + os.path.basename(currfn)))
    if not path: path = '.'
    if verbose: print 'get_version::path2', path

    git = sh.git.bake(_cwd=path)
    return git.describe('--long' ,'--tags', '--dirty', '--always')


if __name__ == '__main__':
    print os.path.basename(os.path.dirname(os.path.abspath(__file__))), get_version(__file__)
