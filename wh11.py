#Numbers

import math
f = open('Numbers.txt', "w")
f.writelines(['1997\n',
'1996\n',
'14\n',
'33\n',
'128\n'])
f = open ('Numbers.txt')
numbers = f.readlines()
summ = int(numbers[0]) + int(numbers[1])
product = round(math.sqrt(int(numbers[2]) * int(numbers[3])))
great = max(summ, product)
cos = math.cos(int(numbers[4]))
print('summ: ' + str(summ))
print('received: ' + str(product))
print('max: ' + str(great))
print('cos: ' + str(cos))
