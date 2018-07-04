while True:
    try:
        xx = raw_input()
        xx = xx.split()[::-1]
        for i in range(len(xx)-1):
            print xx[i],
        print xx[-1]
    except:
        break