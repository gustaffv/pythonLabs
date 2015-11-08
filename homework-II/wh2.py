
studlist = ['Alex Prime', 'Bob Adams',
            'Jack Torsch', 'Jan Blashchich',
            'Petr Osetrov', 'Megan Raion',
            'Alex Qwarz', 'Dazy Yang']
print(studlist)

indexlist = int(input('задайте № студента: '))
print('-', studlist[indexlist])

srlist = input('выбор студентов от - до: ')
sectionlist = srlist.split(' ')
print(studlist[int(sectionlist[0]):int(sectionlist[1])])


p = 0
for i in studlist:
    if 'p' or 'P' in i:
        p >= 1
print('присутствует "p" = ', p)

names = []
for i in studlist:
    name, surname = i.split()
    for name, student in names:
        if name not in names:
          names.append((name, [name, surname]))
print(names)
