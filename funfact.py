def factorial(lmt):
    fact=1
    for i in range(1,lmt+1):
        fact=fact*i
    return "factorial of {} is::{}".format(lmt,fact)
    
lmt=int(input("enter the number"))
print(factorial(lmt))
