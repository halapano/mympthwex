import argparse
import glob
import os
import re

parser = argparse.ArgumentParser(description='grep the pattern from file')

#1TODO:add arguments
parser.add_argument('pattern',type=str)
parser.add_argument('filenames',type=str,nargs='+')

args = parser.parse_args()


pattern = re.compile(args.pattern)

#filenames = glob.glob('./'+args.filenames)
filenames = (args.filenames)

#2TODO:analysis arguments
#read file and match 
#print(args.filenames)
for file in filenames:
    target=open(file)
    #tmpline = target.readlines()
    #print(tmpline)
    #if re.search(pattern,tmpline):
    for line in target:
        if pattern.search(line): 
            print(file,line,end='')
       
     
