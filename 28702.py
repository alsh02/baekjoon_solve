# 28702번: FizzBuzz
import sys

inputs = []
for i in range(3):
    inp = sys.stdin.readline().rstrip()
    try:
        inp = int(inp)
    except:
        pass

    inputs.append(inp)

for i, val in enumerate(inputs):
    if type(val) == int:
        seq = val + 3 - i

        if seq % 3 == 0:
            if seq % 5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif seq % 5 == 0:
            print("Buzz")
        else:
            print(seq)
        break