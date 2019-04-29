'''
return sends the specific value to the caller.
yields retains enough states to enable function to resume where it is left of.
yield produce a sequence of values.we use it when we want iterate through sequence.
but dont want to store entire sequence in the memory.

'''


def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


print("The output i:")
for value in simpleGeneratorFun():
    print(value)




'''The output is:
1
2
3'''