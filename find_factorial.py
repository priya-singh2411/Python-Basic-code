# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 23:25:58 2020

@author: priya singh
"""

def fact(n):
    fact_val=1
    for i in range(1,n+1):
        fact_val=fact_val*i
    return fact_val


x=int(input('Enter Number to find factorial: '))
res=fact(x)
print('factorial for {} is : {}'.format(x,res))
        
