s=input()
count=0
substrings=[]  
current_substring=""
for char in s:
    current_substring +=char
    if char =='L':
        count +=1
    else:
        count -=1

    if count ==0:
        substrings.append(current_substring)
        current_substring =""

print(len(substrings))
for substring in substrings:
    print(substring)