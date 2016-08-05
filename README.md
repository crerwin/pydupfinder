# Dupfinder

A Python script to find duplicate files.  It catalogs all files by name in the specified folder(s), and hashes any files with the same name to confirm that they are duplicates.  Functionality will probably be added to hash everything, so you can catch duplicates that have different names.

## Getting Started

Clone or download the repo.  Execute dupfinder.py:

```
python dupfinder.py /path/to/folder [/path/to/another/folder /path/to/a/third/folder]
```

### OS Compatibility
This should theoretically work on any system running Python3 with file system access.  Tested so far on Windows and OS X.

### Prerequisities

Python 3
