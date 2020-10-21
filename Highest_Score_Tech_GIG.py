# -*- coding: utf-8 -*-

"""
Find the Highest Score among all the players.
This problem statement is from Tech GIG Python Practice.
"""
def main():
    n=int(input())
    lst_val=[]
    for i in range(0,n):
        lst_val.append(int(input()))
    print(max(lst_val))


main()
