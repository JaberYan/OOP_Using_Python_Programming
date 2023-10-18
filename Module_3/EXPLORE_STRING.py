name = 'jaber\'s ahmed'  #escape
name2 = "RIYAN AHMED JABER"
name3 = """
    jaber ahmed riyan
"""
print(name)

for ch in name:
    print(ch)
print()
print(name[2])
print(name[::-1])  #slicing
if 'jaber' in name:
    print('exist')
    
print(name.upper())
print(name2.lower())
print(name2.title())
print(name2.swapcase())
print(name2.capitalize())
#string is sequence if character
#mmutable means changeable
#immutable you can not change it