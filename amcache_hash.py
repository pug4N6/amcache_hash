import sys
import os
import hashlib

# Example Usage: python amcache_hash.py executable_file.exe

# Set max byte size to hash
max_hash_size = 31457280  # 30 MB

# Get file name from command line argument
try:
    file = sys.argv[1]
except Exception as e:
    # If no file provided, exit
    print("|!| No input file provided. Exiting ...")
    print("|?| Example Usage: python amcache_hash.py executable_file.exe")
    exit(1)

# Check if 'file' is actually a file
if os.path.isfile(file):
    # Open file for binary reading 'rb'
    with open(file, 'rb') as f:
        # Check file size vs max hash size
        # If greater than 30 MB, read only the first 30 MB and print the SHA1 hash
        if os.path.getsize(file) > max_hash_size:
            print("|*| File larger than 30 MB, hashing only the first 30 MB ...")
            print(f"|MD5| {hashlib.sha1(f.read(max_hash_size)).hexdigest()}")
        # If less than 30 MB, read the whole file and print the SHA1 hash
        else:
            print("|*| File less than 30 MB, hashing the entire file ...")
            print(f"|MD5| {hashlib.sha1(f.read()).hexdigest()}")
            
# If 'file' was not identified as an actual file, exit
else:
    print(f"|!| {file} was not identified as a valid file. Exiting ...")
    print("|?| Example Usage: python amcache_hash.py executable_file.exe")
    exit(1)
