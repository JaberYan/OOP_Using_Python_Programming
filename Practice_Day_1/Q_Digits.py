t=int(input())
for i in range(t):
    num=input()
    rever_string=reversed(num)
    # print(list(rever_string))
    for value in rever_string:
        print(value,end=' ')
    print()