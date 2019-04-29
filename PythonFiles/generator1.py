
'''
generate squares from 1 to 100 using yield hence generator
generator: is a function is defined like a normal one but whenever it needs to generate a value, it does so
by yield keyword rather than return.
'''

def nextSquare():
    i=1

    while True:
        yield i*i
        i+=1


for num in nextSquare():
    if num>100:
        break
    print(num)

