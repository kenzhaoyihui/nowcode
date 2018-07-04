import operator

while True:
    try:
        n = int(raw_input())
        x1 = {}
        for i in range(n):
            a, b = raw_input().split()
            if int(a) not in x1.keys():
                x1[int(a)] = int(b)
            else:
                x1[int(a)] += int(b) 
        s = sorted(x1.items(), key=operator.itemgetter(0))
        for i in range(len(s)):
            print s[i][0], s[i][1]
    except:
        break