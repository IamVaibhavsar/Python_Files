class myClass:
    __hiddenVar=0       #(__ for data hiding: these attributes not directly visible outside.)

    def add(self,increment):
        self.__hiddenVar+=increment
        print(self.__hiddenVar)



myObject=myClass()
myObject.add(2)         #2
myObject.add(5)          #7

#print(myObject.__hiddenVar)             #ERROR
print(myObject._myClass__hiddenVar)     #7 TRICKY SYNTAX

#nthing in python is truely private





















