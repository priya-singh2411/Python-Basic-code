"""
This Program is from Hackerrank Python practice problems on lists.
"""
if __name__ == '__main__':
    N = int(input())
    lst=[]
    for i in range(N):
        input_lst=input().strip().split(" ")
        if input_lst[0] =='insert':
            lst.insert(int(input_lst[1]),int(input_lst[2]))
        if input_lst[0] == 'remove':
            lst.remove(int(input_lst[1]))
        if input_lst[0] == 'append':
            lst.append(int(input_lst[1]))
        if input_lst[0] =='sort':
           lst= sorted(lst,reverse=False)
        if input_lst[0] =='pop':
            lst.pop()
        if input_lst[0] == 'reverse':
            lst.reverse()
        if input_lst[0] =='print':
            print(lst)
    

"""
Sample Input:
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
"""