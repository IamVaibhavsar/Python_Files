male=False
tall=True

if male and tall:
    print("You are a tall male")
elif male and not(tall) :                            #else if
    print("you are short male")
elif not(male) and tall:
    print("You are tall female")
else:
    print("You are short female")