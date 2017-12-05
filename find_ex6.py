#TODO: some module
#import argparse
#import subprocess
#import glob


import argparse
import os
import fnmatch
import glob

parser = argparse.ArgumentParser(description='find files')

parser.add_argument('filepath',metavar = 'PATH',type=str)

#parser.add_argument('-name',type = str,action="store_true")

parser.add_argument('filename',type=str)

args = parser.parse_args()

fipt = args.filepath

fina = args.filename

for file in os.listdir(fipt):
    if fnmatch.fnmatch(file,fina):
        print(file)



