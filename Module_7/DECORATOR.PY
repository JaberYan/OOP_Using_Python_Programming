import math
import time

def amni(func):
    def amni_arki(n):
        print('time started')
        start = time.time()
        # print(func)
        func(n)
        print('time ended')
        end = time.time()
        print(f'total time taken {end-start}')
    return amni_arki

# amni()()

@amni
def get_function(n):
    print('the function is working')
    result = math.factorial(n)
    print(f'factorial of {n} is : {result}')

# amni(get_function)()
get_function(5)