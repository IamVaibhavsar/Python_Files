class CSStudent:
    stream="cse"

    def __init__(self,roll):        #(__ for data hiding: these attributes not directly visible outside.)
        self.roll=roll
        #self.address=address

    def setadress(self,address):
        self.address=address

    def getadderss(self):
        return self.address

a=CSStudent(101)
#b=CSStudent(102)
print([a])

print(a.stream)
a.setadress("Nashik,MH")
#print(b.roll)
print(a.getadderss())           #nashik,MH





#empty class

class empty:
    pass

