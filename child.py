import sys
word = sys.stdin.readline().rstrip()
filename = sys.stdin.readline().rstrip()
try:
    with open(filename, 'rb') as fh:
        while True:
            current = fh.readline()
            if not current:
                break
                print(f'find: {filename} {word}')
except:
    pass
