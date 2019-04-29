#simple Iterator example that iterates from 10 to given limit value
#iterator:any python type that can be used with a "a for loop"
#lists,touples,dictionaries are all inbuilt iterators


class Test:

    def __init__(self,limit):           #constructor
        self.limit=limit


    def __iter__(self):             #iter is a menthod to iteration is initialised, returns an object
        self.x=10
        return self

    def __next__(self): #to move to next element,returns next value, should raise stopiteration to signal end of the iteration

        x=self.x                #store current value of x

        if x>self.limit:
            raise StopIteration         #if limit reached, stop iteration

        self.x=x+1          #else increment and return old value
        return x


for i in Test(15):      #10 11 12 13 14 15
    print(i)

for i in Test(5):
    print(i)
