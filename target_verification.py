#!./lib/python.exe
"""
based on the results - it should be possible to generate a new variant of the hashlib - I'll hash all of the files that match the various parameters,
and then make sure that the output should be written to a directory excluded...

no main loop for now.
"""
import hashlib;
import os;
import sys;
import time;

def os_walk_test(directory):
    st = (time.strftime('%H:%M:%S'),time.time())
    slices = [];
    for a in os.walk(directory):
        slices.append((time.strftime('%H:%M:%S'),time.time()))
    fn = (time.strftime('%H:%M:%S'),time.time())
    delta = (fn[1]-st[1])
    print(delta)
    return st,fn,delta
    
def find_files_of_type(directory:"path to begin seeking in"=".", types:"list of types to look for - will default to finding all files."=['']):
    """
    identify the path of certain types.
    """
    if not os.path.isdir(directory): raise ValueError("directory must be a valid path on this machine!");
    if not type(types)==list: raise ValueError("types must be a list of strings");
    for a in types:
        if not type(a)==str: raise ValueError("types must be a list of strings");
    # path, directories, files; # use os.walk()[1]
    files = [];
    paths = [];
    try:
        for a in os.walk(directory):
            paths.append(a[0]);
            #print(a)
            for b in a[2]:
                for c in types:
                    if c.lower() in os.path.basename(b).lower(): 
                        files.append(a[0]+os.sep+b);
                        break; # break out of the inner loop and continue the outer loop if it finds a match.
    except IndexError as IE:
        raise Exception(str(IE)+' Not quite sure how this one happened')
    except Exception as EE:
        raise Exception(str(EE)+' here is the inner exception stack trace...')
    return files;
    

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
    
def dir_ver2(directory_path,output_path = None,file_types = ['']):
    """
    upgraded version of dir_ver for use in environments that do not
    need to have a new hash file written into each directory.
    additionally, will use os.walk to traverse directories.
    """
    pass
    output_path = output_path or os.path.abspath('.')+os.sep+"file_values"
    files_2_check = find_files_of_type(directory_path,file_types);
    combos = []; # order will be hash, filepath;
    for a in files_2_check:
        try:
            with open(a,'rb') as data:
                hash = hashlib.sha256(data.read()).hexdigest();
                m_dt = os.path.getmtime(a)
                m_sz = os.path.getsize(a)
            combos.append((hash,m_dt,m_sz,a));
            print(hash+' '+a);
        except Exception as ECHO:
            print(ECHO);
    with open(output_path,'a') as data:
        data.write("value\tmodified\tsize\tpath\n")
        for a in combos:
            #data.write("%s\tmodified:%s\tsize:%s\tpath:%s\n"%(a[0],a[1],a[2],a[3]))
            data.write("%s\t%s\t%s\t%s\n");            
    return combos;