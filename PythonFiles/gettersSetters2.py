class C(object):
    def __init__(self):
        self._x=None

    @property
    def x(self):
        print("Getter of x called")
        return self._x

    @x.setter
    def x(self,value):
        print("setter of a called")
        self._x=value

    @x.deleter
    def x(self):
        print("deleter of x called ")
        del self._x


c=C()
c.x='foo'
foo=c.x
del c.x

'''setter of a called
Getter of x called
deleter of x called '''