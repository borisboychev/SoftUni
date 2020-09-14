import os

try:
    os.remove('text.txt')
    print('File deleted')
except:
    print('No such file')