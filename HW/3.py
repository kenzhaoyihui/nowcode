# x = int(raw_input())

# a = []
# while x>0:
#     z = int(raw_input())
#     a.append(z)
#     x -= 1

# print "\n"

# for i in sorted(set(a)):
#     print i

import sys

while True:
    try:
        n = int(sys.stdin.readline())
        a = []
        for i in range(n):
            a.append(int(sys.stdin.readline()))
        result = sorted(set(a))
        for i in result:
            print i
    except:
        break

