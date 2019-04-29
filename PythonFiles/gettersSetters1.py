'''
1.make members public  OR
2.let the members be private and use getters and setters so that they can be retrieved and changed later on
to change the implementation without changing the interface
python has implicit getters and setters
Getters and setters: data encapsulation(packaging of data with the methods manipulating them)
mutator methods

getter:retrieving the data
setter:changing the data
attributes of the class are made private to protect from other code

getter function: @property
setter function: @x.setter
'''


#JAVA style
class Square(object):
    def __init__(self,length):
        self.length=length

    def getter_length(self):        #getter
        return self._length


    def setter_length(self,length):        #Setter
        self._length=length

r=Square(5)
r.getter_length()
r.setter_length(10)





