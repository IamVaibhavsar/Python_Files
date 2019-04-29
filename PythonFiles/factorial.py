num=int(input("Enter the number whose factorial youwant to calculate:"))
factorial=1

if num<0:
    print("Factorial of negative number does not exist.")

elif num==0:
    print("Factorial of",num,"is = 1")

else:
    for i in range(1,num+1):        #loop iterates from 1 to num
        factorial=factorial*i

    print("The factorial is", num,"!=",factorial)