# -*- coding: utf-8 -*-
def loader(fname, cut = 0, top = float('inf')):
    data = dict()
    with open(fname, 'r') as f:
        i=0
        for x in f:
            if not i%1000000:
                print(i)
            i+=1
            if i > top:
                break
            num, key, key2 = x.split()
            if int(num) > cut:
                if key not in data:
                    data[key]=dict()
                data[key][key2] = num
    return data


def loader3(fname, cut = 0, top = float('inf')):
    data = dict()
    with open(fname, 'r') as f:
        i=0
        for x in f:
            if not i%1000000:
                print(i)
            i+=1
            if i > top:
                break
            a = x.split()
            if len(a) == 4:
                num, key, key2, key3 = a
    #             print(num, key, key2, key3)
                if int(num) > cut:
                    if key not in data:
                        data[key]=dict()
                    if key2 not in data[key]:
                        data[key][key2]=dict()

                    data[key][key2][key3] = num
    return data

