class Addition:
    first=0
    second=0
    ans=0

    def __init__(self,f,s):     #parameterised constructor
        self.first=f
        self.second=s

    def display(self):
        print("The first number=",self.first )
        print("The second number=",self.second)
        print("Addition of two numbers is=",self.ans)

    def calculate(self):
        self.ans=self.first+self.second


obj=Addition(100,230)
obj.calculate()
obj.display()

'''
The first number= 100
The second number= 230
Addition of two numbers is= 330'''