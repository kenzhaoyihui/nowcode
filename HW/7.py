while True:
    try:
        x = raw_input()
        if int(str(x).split('.')[1][0])>=5:
            print int(str(x).split('.')[0])+1
        else:
            print int(str(x).split('.')[0])
    except:
        break