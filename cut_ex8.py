import argparse

#TODO: add argument
# -d
# -f

parser = argparse.ArgumentParser()
parser.add_argument('-d',type=str)
parser.add_argument('-file',metavar = 'file',type=str)

group = parser.add_mutually_exclusive_group()
group.add_argument('-f',type=str)

args = parser.parse_args()


print(args.d,args.f,args.file)

#print(args.d,args.file,args.f)
#delimeter = args.d
#filename = args.f
#in_file = open(filename)
#for line in in_file:
#    wordlist = line.split



