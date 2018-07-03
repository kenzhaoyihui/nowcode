
x1 = raw_input()
x2 = raw_input()

if x2.lower not in x1.lower:
    print 0
else:
    count = 0 
    for i in x1:
        if i == x2:
            count += 1
    print count

