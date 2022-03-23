#List Files in a directory
import os

path = '/home/dwight/scripts'

files = os.listdir(path)
for file in files:
    print(file)