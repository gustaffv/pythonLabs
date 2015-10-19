#Diameters

import math
pi = math.pi

diameters = 45, 338, 19
area1 = pi / 4 * (diameters [0] ** 2)
area2 = pi / 4 * (diameters [1] ** 2)
area3 = pi / 4 * (diameters [2] ** 2)
print(area3, area2, area1)
results = (area2 + area1) - area3
print(results)
    f = open('result.txt', "w")
    f.write('')
    f.close()
