while True:
    try:
        xx = int(raw_input())
        xx_2 = str(bin(xx))
        count = 0
        for i in xx_2:
            if i == '1':
                count += 1
        print count
    except:
        break
