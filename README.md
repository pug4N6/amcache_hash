A few articles/blogs recently identified that the hash values stored with Amcache information was only for the first 30 MB of a file (if the file was larger than 30 MB). 

https://www.reddit.com/r/computerforensics/comments/sq6xls/amcache_sha1_mismatch/

http://windowsir.blogspot.com/2022/02/the-misuse-of-artifact-categories.html

So, I created a simple Python script to calculate the hash value of a file based on this information.

Usage: amcache_hash.py executable_file.exe
