# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 15:26:47 2020

@author: priya singh
"""


def countingValleys(steps, path):
    # Write your code here
    valey = sea_lvl = 0
    for stp in  path:
        if stp == 'U':
            sea_lvl+=1
        else:
            sea_lvl+=-1
        if stp == 'U' and sea_lvl == 0:
            valey+=1
    return valey

steps=8
path='UDDDUDUU'
res=countingValleys(steps, path)
print('valeys covered: {}'.format(res))
