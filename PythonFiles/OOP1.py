class Test :
    def fun(self):      #self: mandatory argument.python provides value for self parameter
        print("Hello")


obj=Test()
obj.fun()

#Hello

class person:
    def __init__(self,name):
        self.name=name

    def say_hi(self):
        print("Hello,my name is", self.name)

p=person("vaibhav")
p.say_hi()

#Hello,my name is vaibhav
