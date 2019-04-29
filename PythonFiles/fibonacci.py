# 0 1 1 2 3 5 8 13 21 34

nterms=int(input("Enter the number of terms:"))

n1=0
n2=1
count=0

if nterms <=0:
    print("Please enter a positive number.")

elif nterms==1:
    print("Fibonacci series upto", nterms,":")
    print(n1)

else:
    print("Fibonacci series upto", nterms," is:")
    while count< nterms:
        print(n1,end=',')   #end= in python print statement ends with newline bydefault.
                            #end parameter is used to avoid that .
        nth= n1+n2
        n1=n2
        n2=nth
        count+=1
