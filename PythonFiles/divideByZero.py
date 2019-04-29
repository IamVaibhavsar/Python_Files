try:
    answer=50/0
    number=int(input("Enter the number: "))
    print(number)

except ZeroDivisionError as err:
    print(err)                      #ZeroDivisionError and ValueError are predefined in python
except ValueError :
    print("INVALID INPUT!")


'''OR
except ZeroDivisionError:
    print("Divide by zero")

except ValueError:
    print("INVALID INPUT")'''



