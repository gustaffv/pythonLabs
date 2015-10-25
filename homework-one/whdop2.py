
a = [1, -20, 38, 0, 44]
b = [88, -20, 48, 4, 33, 2]
for x, y in zip(a, b):
    print (x, y)
    if abs(x - y) < 15:
        print ('BINGO')
    if x < y:
        print (x)
    elif x == y:
         continue
    else:
        print (x)
