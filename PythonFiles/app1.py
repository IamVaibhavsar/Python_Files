from chef import Chef
from chinese import ChineseChef

myChef =Chef()
myChineseChef=ChineseChef()

myChef.make_chicken()
myChineseChef.make_fried_rice()


myChineseChef.make_chicken()        #we can inherit all the features of the base class.

myChineseChef.make_special_dish()
myChef.make_special_dish()

'''The chef makes a chicken.
The Chef makes fried rice 
The chef makes a chicken.
The chef makes the special dish barbeque        
    #if same function is present in derived class then the the function of derived class gets executed.
    otherwise the function of base class gets inherited.
The chef makes the special dish barbeque'''