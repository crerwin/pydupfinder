__author__ = 'Chris Erwin'

import os
import sys
import getopt
import hashlib
from collections import defaultdict

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

def inventoryFilesByName(path, filesByName):
    print("inventorying ", path)
    for directory, subdirectories, files in os.walk(path):
        for file in files:
            filesByName[file].append(directory)

def main():
    if len(sys.argv) > 1:
        folders = sys.argv[1:]
        filesByName = defaultdict(list)
        filesByHash = defaultdict(list)
        print("building list of possible dupes by name")
        for path in folders:
            if os.path.exists(path):
                inventoryFilesByName(path, filesByName)
            else:
                print(path, " is not valid")
                sys.exit()
        print("hashing possible dupes.  Number of files: ", len(filesByName))
        count = 0
        for file in filesByName:
            count += 1
            print(count, end='\r')
            if len(filesByName[file]) > 1:
                for path in filesByName[file]:
                    filesByHash[(getHash(os.path.join(path, file)))].append(os.path.join(path, file))
        for hash in filesByHash:
            if len(filesByHash[hash]) > 1:
                print(file, filesByHash[hash])


    else:
        print("Usage: dupfinder.py folder [folder2 folder3...]")

if __name__ == '__main__':
    sys.exit(main())
