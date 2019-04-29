#chaining of the multiple decorators.

def star(func):
    def inner(*args,**kwargs): # these arguments are given so that it can decorate any kind of function with all kinds and n number of argument.

        print("*"*30)
        func(*args,**kwargs)
        print("*"*30)
    return inner

def percent(func):
    def inner(*args,**kwargs):
        print("%"*30)
        func(*args,**kwargs)
        print("%"*30)
    return inner


#a function can be decorated multiple times with same(or different)
@percent
@star
def printer(msg):       # is equal to star(percent(printer))
    print(msg)


printer("Hello")

'''
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
******************************
Hello
******************************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'''
