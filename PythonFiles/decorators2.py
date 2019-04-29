'''
functions and methods are called callable
any object implements the special method __call__() is termed callable.
decorator: is a callable that returns a callable
acys as a gift wrapper.

'''

def make_pretty(func):      #decorator
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("i am ordinary")      #i am ordinary


#lets decorate ordinary
pretty=make_pretty(ordinary())
pretty()

#i got decorated
#i am ordinary