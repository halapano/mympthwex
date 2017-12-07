import sys


lines = []
while True:
    try:
        line  = input()
        lines.append(line)
    except EOFError:
        break
    except IndexError:
        pass


uniqLine = list(set(lines))
uniqLine.sort(key = lines.index)
for name in uniqLine:
    print(name)
