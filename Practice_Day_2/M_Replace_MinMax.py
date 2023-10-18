n=int(input())
list_list=list(map(int,input().split()))
x=list_list.index(max(list_list))
y=list_list.index(min(list_list))
list_list[x],list_list[y]=list_list[y],list_list[x]
for value in list_list:
    print(value,end=' ')