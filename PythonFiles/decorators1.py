'''
decorators(metaprogramming): callable python object used to modify class or a function.
adds functionality and returns it.

everything in python(classes,functions as well) are objects.
'''

def succ(x):
    return x+1

successor=succ          #2 names for a function
print(successor(10))        #11

print(succ(10))             #11

#Functions as arguments

def inc(x):
    return x+1

def dec(x):
    return x-1

def operate(func,x):
    result=func(x)
    return result

operate(inc,3)      #4
operate(dec,3)      #2


#function returning another function

def is_called():
    def is_returned():
        print("hello")
    return is_returned()        #function is returned

new=is_called()

new()           #output:hello