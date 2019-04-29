#python does not support switch and case statement to we use dictionary mapping

def numbers_to_strings(argument):
    switcher={
        0:"Zero",
        1:"One",
        2:"Two",
        3:"Three",
        4:"Four",
}
    return switcher.get(argument,"nothing")

'''
get() function of dictionary data type returns value of passed argument if it is present in dixtionary.
otherwise second argument will be assigned as default value of passed argument'''

if __name__ =="__main__":
    number=int(input("Enter the number:"))
    print(numbers_to_strings(number))


#Enter the number:2
#Two

#Enter the number:10
#nothing