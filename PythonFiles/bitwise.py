num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

num3=0

num3= num1 & num2            #AND
print("the answer is =",num3)

num3= num1 | num2              #OR
print("the answer is =",num3)

num3= num1 ^ num2             #XOR
print("the answer is =",num3)

num3= ~num2                #secondary complement form
print("the answer is =",num3)

num3= num1 << 2            #left shift by 2 bits
print("the answer is =",num3)

num3= num1 >> 2            #right shift by 2 bits
print("the answer is =",num3)

num3= num1// num2         #floor division: whole number adjusted to the left in the number line
print("the answer is =",num3)

num3= num1 ** num2
print("the answer is =",num3)