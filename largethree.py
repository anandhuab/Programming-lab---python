#largest of three
a=int(input("Enter the value of a::"))
b=int(input("Enter the value of b::"))
c=int(input("Enter the value of c::"))
if a>b and a>c:
    print("{} is greatest".format(a))
elif b>a and b>c:
    print("{} is greatest".format(b))
else:
    print("{} is greatest".format(c))
    
