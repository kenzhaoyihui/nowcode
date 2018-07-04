while True:
    try:
        a = []
        xx = raw_input()
        for i in set(xx):
            if ord(i)>=0 and ord(i)<=127:
                a.append(i)
        print len(a)
    except:
        break