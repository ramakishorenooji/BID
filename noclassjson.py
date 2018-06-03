import json


def Jread():
    with open('sample.json','r') as fp:
        obj = json.load(fp)
    print(type(obj))
    print(obj)


Jread()
