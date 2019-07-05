"""
this is for super basic tests
mainly like one-liners
or basic functions that I should know
kinda like adding 2+1
gotta make sure it works
"""

list = [1,2,3,4,5]




for i in range(6):
    list.insert(0, i)
    if len(list) > 5:
        del list[-1]
    print(list)