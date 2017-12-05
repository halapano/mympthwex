import sys
import glob


#ls -l | sed -e "s/halapano/author/g"

_,script = sys.argv


cut = script.split('/')
 = cut[0]
new = cut[1]

while True:
    try:
        line = input()
        newline = line.replace(old,new)
        print(newline)

    except EOFError:
        sys.exit(0)
    except IndexError:
        pass

