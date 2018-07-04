while True:
    try:
        n = int(raw_input())
        a = []
        for i in range(n):
            xx = raw_input()
            a.append(xx)
        for i in sorted(a):
            print i
    except:
        break