#!/usr/bin/python3
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
        try:
            name = os.path.basename(a);
            hash = ""
            with open(a,'rb') as data:
                hash = hashlib.sha256(data.read()).hexdigest();
            name_hashes.append((name,hash)); # should add the hash to the file
        except Exception as ECHO:
            print("Looks like it was a directory.. %s"%(str(ECHO)))
    with open("hashes","w") as hashes:
        for a in name_hashes:
            hashes.write("File: %s\tHash: %s\n"%(a[0],a[1]));
    return name_hashes;

def no_args():
    """
    run this component if there aren't any args in sys.argv (aside from the
    name )
    """
    pass
    print("press ctrl+c to exit");
    cont = 'y' #input("Would you like to validate a directory (y/n): ")
    while cont.lower() == 'y':
        directory_path = input("Enter the directory to validate: ");
        x = dir_ver(directory_path);
        for a in x: print("Name: %s Hash: %s"%(a[0],a[1]));
        cont = input("Would you like to validate a directory (y/n): ")

def as_main():
    """
    run the function if it is the main program on the stack.
    """
    pass
    x=[]
    for a in sys.argv[1:]:
        x+=dir_ver(a); # run the verification over the arbitrary directory.
    for b in x: print("Name: %s Hash: %s"%(b[0],b[1]));

if __name__=="__main__":
    if len(sys.argv) > 1:
        as_main();
    else:
        no_args();
    
        
