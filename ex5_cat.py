import argparse

parser = argparse.ArgumentParser(description='concatenate')
parser.add_argument("filename",type =str,nargs='*')

args = parser.parse_args()
    
for file in args.filename:
    infile = open(file,'r')
    print(infile.read(),end="")


