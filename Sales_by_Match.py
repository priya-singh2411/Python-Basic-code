# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 00:02:35 2020

@author: priya singh
"""
import math
import os
import random
import re
import sys



# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    s_lst=list(set(ar))
    pair_var=0
    for i in range(0,len(s_lst)):
        var1=s_lst[i]
        val=ar.count(var1)//2
        pair_var=pair_var+val
    return pair_var
        #print('pair: {}'.format(pair_var))
        



ar=[1,2,1,2,2,2,1,3,2]
res=sockMerchant(7, ar)
print('No of pairs are : ',res)