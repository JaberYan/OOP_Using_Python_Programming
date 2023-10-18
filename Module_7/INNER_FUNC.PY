def inner__deckar():
    print('starting the inner function')
    def inner_func(a,b):
        print('another the inner function in inner_deckar{a+b}')
    return inner_func
        
# print(inner__deckar()(6,7))

def do_something(work):
    print('work started')
    work(9)
    print('work ended')
    
def coding(a):
    print('write a code using python',a)
    
do_something(coding)