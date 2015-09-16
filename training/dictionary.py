# -*- coding: utf-8 -*-
__author__ = 'Vietworm'


def dic():
    #d = {1: 'Javascript', 5: 'Python', 3: '.NET', 4: 'C/C++', 2: 'NodeJS', 6: 'Java'}
    d = dict(
        one='Javascript',
        two='Python',
        three='.NET',
        four='C/C++',
        five='NodeJS',
        six='Java'
    )
    d['seven'] = 7
    v = 'sixs'
    print('get property: ', d.get(v, 'Dictionary keys not found'))
    for item in sorted(d.keys()):  #Auto using built-in function sorted and apply to keys dictionary - sorted(d.keys())
        print("{0}: {1}".format(item, d[item]))

if __name__ == "__main__":
    dic()