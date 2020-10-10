# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 00:14:26 2020

@author: priya Singh
"""
#This Code is to print the fibonacci series for any of the given number in the input
def fibonacci_num(num1):
    a=0
    b=1
    if num1<0:
        print("Invalid Input!",end=" ")
    elif num1==0:
        print(a,end=" ")
    elif num1==1:
        print(a,end=" ")
        print(b,end=" ")
    else:
        print(a,end=" ")
        print(b,end=" ")
        for i in range(2,num1):
            c=a+b
            a=b
            b=c
            print(c,end=" ")
        
    
n=int(input("Enter the number for Fibonacci series to print: "))    
fibonacci_num(n)