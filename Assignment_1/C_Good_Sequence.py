import collections
N = int(input())
arr = list(map(int,input().split()))

element_counts = collections.Counter(arr)
remove_element = 0 
for x,count in element_counts.items():
    # print(x,':',count)
    if x>count:
        remove_element += count
    if x<count:
        remove_element += count-x
print(remove_element)
    
