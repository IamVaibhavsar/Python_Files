#fibonacci series by generator function

def fibonacci(limit):

    a,b=0,1

    while a<limit:
        yield a
        a,b=b,a+b

#x=fibonacci(10)
#print(x.__next__())             # 0

print("Using the for loop:")
for i in fibonacci(20):
    print(i)

'''
Using the for loop:
0
1
1
2
3
5
8
13
'''

'''
advantage of generator:
efficient  memory usage
no need to write iter amd next methods
'''