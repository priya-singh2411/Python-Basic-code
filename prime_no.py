# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 20:50:53 2020

@author: pritz
"""
import math

def calc_prime(num):
    n=int(math.sqrt(num))
    for i in range(2,n+1):
        if num%i==0:
            print('Not a prime number')
            break
    else:
        print('prime number')
        
def prime_range(num):
    #n=int(math.sqrt(num))
    for i in range(2,num):
        if i%2!=0:
            print(i)
            # break 
        
    
    
input_val=int(input("Enter 1 to find the number is prime or not AND Enter 2 to find the list of prime numbers: "))    

if input_val==1:
    num=int(input("Enter the Number to find for Prime Number: ") )   
    calc_prime(num)
elif input_val==2:
    num=int(input("Enter the Number to find for List of Prime Numbers: ") )   
    prime_range(num)
    #print("Under Construction!!")
else:
    print("Invalid Input!")
