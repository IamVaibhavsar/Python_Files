def exponent(base,pow):
    result=1
    for index in range(pow):            #number of iterations
        result=result*base
    return result


base=int(input("Enter the base: "))
power=int(input("Enter the power or exponent:"))
ans=exponent(base,power)
print(ans)