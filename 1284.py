import sys

while True:
    N = sys.stdin.readline().rstrip()

    if int(N) == 0:
        break
    
    length = 1 + len(N)
    
    for digit in N:
        d = int(digit)
        
        if d == 1:
            length += 2
        elif d == 0:
            length += 4
        else:
            length += 3
    
    print(length)