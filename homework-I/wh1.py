import os

files = os.listdir('.')
result = open('result.txt', "w")
n = 0
for name in files:
    if name.count('python'):
        print(name)
        result.write('files питоны: ' + name + '\n')
        overal = n + name.count('python')
print(overal)
result.write('overal: ' + str(overal) + '\n')
result.close()
