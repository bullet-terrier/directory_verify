"""
dir_ver: module to load a directory, and generate hashes of its contents.
"""

import hashlib;
import os;
import sys;

def dir_ver(directory_path):
    """
    dir_ver - pass in a directory - will generate a file to contain
    the hashes.

    currently will only support sha256, will expand later.
    """
    pass
    os.chdir(directory_path)
    name_hashes = [];
    path_files = os.listdir(directory_path);
    for a in path_files:
        name = os.path.basename(a);
        hash = ""
        with open(a,'rb') as data:
            hash = hashlib.sha256(data.read()).hexdigest();
        name_hashes.append(tuple(name,hash)); # should add the hash to the file
    return name_hashes;

def wrt_ver(name_hashes):
    """
    generate the file for storing in the files.
    """

def no_args():
    """
    run this component if there aren't any args in sys.argv (aside from the
    name )
    """
    pass
    cont = input("Would you like to validate a directory (y/n): ")
    while cont.lower() == 'y':
        

def as_main():
    """
    run the function if it is the main program on the stack.
    """
    pass

if __name__=="__main__":
    if sys.argv.len() > 1:
        as_main();
    else:
        no_args();
    
        
