#coding: utf-8

class Tank:
    def __init__(self, tracks = bool, model = str, speed = int):
        self.tracks = tracks
        self.model = model
        self.speed = speed

    def status(self):
        print('Tank', self.model, 'Tracks', self.track, 'Speed', self.speed)
        if self.speed > 0 and self.track is True:
            print('ok')
        else:
            print('error')

class Car:
    def __init__(self, wheels = 4, speed = int, model = str):
        self.wheels = wheels
        self.speed = speed
        self.model = model

    def status(self):
        print('Speed', self.speed, 'Wheels', self.wheels, 'Model', self.model)
        if self.speed > 0 and self.wheels == 4:
            print('ok')
        else:
            print('error')

class Diligence:
    def __init__(self, wheels = int, speed = int):
        self.wheels = wheels
        self.speed = speed

    def status(self):
        print('Wheels', self.wheels, 'Speed', self.speed)
        if self.wheels == 4 and self.speed > 0:
            print('ok')
        else:
            print('error')

PzKpfwV = Tank (tracks = 10, model = 'Panther', speed = 46)
Tesla = Car (speed = 100, model = "X")
Diligence = DiligenceII (speed = 28, model = 2)

carslist = [PzKpfwV, Tesla, Diligence]

for c in carslist:
    c.status()

PzKpfwV.tracks = False
Tesla.speed = 180
Diligence.model = 3

for c in cars:
    c.status()
