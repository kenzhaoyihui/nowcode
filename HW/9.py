while True:
    try:
        xx = raw_input()
        a = []
        for i in xx[::-1]:
            if i not in a:
                a.append(i)
        print int(''.join(a))
    except:
        break
