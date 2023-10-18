# def doubled(x):
#     return x*2

doubled = lambda num : num*2

result = doubled(5)
# print(result)

perametre = lambda num,num2,num3:num*num2*num3
res=perametre(4,5,2)
# print(res)

numbers=[1,2,3,4,5,6,6,10,9,10]
numbers_nums =map(lambda num:num*num,numbers)
# print(numbers)
# print(list(numbers_nums))

actors=[
    {'name':'jaber','age':45},
    {'name':'ahmed','age':40},
    {'name':'riyan','age':50},
]
# junior = filter(lambda x:x['age']<=45,actors)
junior = map(lambda x:x['age']<=45,actors)
fiver = filter(lambda actor:actor['age']%5==0,actors)
# print(list(fiver))
# print(list(junior))
numbers_i=[num for num in actors]
# print(numbers_i)

txt='jaber ahmed riyan'
src='a'
index =txt.find(src)
if(index==-1):
    print("Not Found")
else:
    print(f'the charecter {src} are found and index is {index}')