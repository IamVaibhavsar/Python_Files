#decorate functions that takes parameters

def smart_divide(func):
    def inner(a,b):
        print("i am going to divide",a,"and",b)
        if b==0:
            print("cant divide!")

            return
        return  func(a,b)
    return inner


@smart_divide
def divide(a,b):
    return a/b

divide(2,5)

divide(2,0)

'''
i am going to divide 2 and 5
i am going to divide 2 and 0
cant divide!'''