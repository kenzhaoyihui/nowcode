while True:
    try:
        i = 2
        num = int(raw_input())
        while num>1:
            if num%i==0:
                print i,
                num = num/i
            else:
                i += 1
    except:
        break