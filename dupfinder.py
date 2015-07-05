__author__ = 'Chris Erwin'

import os
import sys
import getopt
import hashlib

def getHash(path, blocksize = 65536):
    #this only works for files that fit in Python's working memory
    #instead used block reading as found here: http://www.pythoncentral.io/finding-duplicate-files-with-python/
    #return hashlib.md5(open(path, 'rb').read()).hexdigest()
    file = open(path, 'rb')
    hasher = hashlib.md5()
    buffer = file.read(blocksize)
    while len(buffer) > 0:
        hasher.update(buffer)
        buffer = file.read(blocksize)
    file.close()
    return hasher.hexdigest()



if __name__ == '__main__':
    if len(sys.argv) > 1:
        folders = sys.argv[1:]
        for path in folders:
            if os.path.exists(path):
                print(path)
                for root, dirs, files in os.walk(path):
                    for file in files:
                        hash = getHash(os.path.join(root, file))
                        print(os.path.join(root, file), hash)
            else:
                print(path, " is not valid")
                sys.exit()
    else:
        print("Usage: dupfinder.py folder [folder2 folder3...]")
