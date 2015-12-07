#coding: utf-8
import os

def find(rash='.txt'):
    for filename in os.listdir('.'):
        if filename.endswith(rash):
            for i, line in enumerate(open(filename),1):
                #читает построчно
                yield filename, i, line,

def grep(gen, substr):
    for name, i, s in gen
        if substr in s:
            yield name, i, s,

for name, i, s in grep(gen=find('.py'), substr = 'def'):
    print(name, i, s)
