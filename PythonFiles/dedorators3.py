import decorators2


#syntactical sugar
@make_pretty        #use @ symbol along with name of decorator and place it above thr function to be decorated.
def ordinary():
    print("I am ordinary")

#is equivalent to
def ordinary():
    print("I am ordinary")
ordinary=make_pretty(ordinary)