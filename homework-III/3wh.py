import os, pickle, sys

basiscarsfile = 'basecar.pickle'
carslist = {
'nameCar':['Tesla', 'DMC'],
'power':['288', '132'],
'numreg':['5PPP064','BS2J005']
}

f = open(basiscarsfile, 'wb')
pickle.dump(carslist, f)

f = open(basiscarsfile, 'rb')
carslist = pickle.load(f)
something = input('Выберите, "R"- записать; "V"- показать: ')
if something == 'V':
    with open (basiscarsfile, 'rb') as f:
        carslist = pickle.load(f)
        carslistsort = sorted (carslist)
        print(carslistsort)
        for key in sorted(carslist, key=lambda key: int(nameCar[key])):
            print(key, nameCar[key])

        hpent = int(input ('Укажите мощность :'))
        carlist = []
        for key in carlist:
            if  int(carlist[key]) == hpent:
                    carlist.append([key,carslist[key]])
        print(carlist)
        carlist = []
        for key in carslist:
            if int(carslist[key]) > hpent:
                carlist.append([key,carslist[key]])
        print('Мощность больше указанной: ', carlist)
        carlist = []
        for key in carlist:
            if int(carslist[key]) < hpent:
                carlist.append([key,carslist[key]])
        print('Мощность меньше указанной: ', carlist)

        nameput = input('Укажите модель автомобиля: ')
        for key in carslist:
            if nameput in key:
                print(key, carslist[key])
        for key in carslist:
            if nameput == key:
                print(key, carslist[key])

if something == 'R':
    with open (basiscarsfile, 'rb') as f:
        carslist = pickle.load(f)
        namecar = input('Укажите модель автомобиля: ')
        if namecar.isalpha() == False:
            print('Попробуйте снова.')
        hp = input('Укажите мощность автомобиля: ')
        if hp.isdigit() == False:
            print('Попробуйте снова.')
        numreg = input('Укажите регистрационный номер автомобиля: ')
        if numreg.isalnum() == False:
            print('Попробуйте снова.')
