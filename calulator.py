#calculator
a=float(input("enter first number:::"))
b=float(input("enter second number:::"))
choice=input("enter the choice")
if choice=='+':
    c=a+b
    print("{}+{}={}".format(a,b,c))
elif choice=='-':
    c=a-b
    print("{}-{}={}".format(a,b,c))
elif choice=='*':
    c=a*b
    print("{}*{}={}".format(a,b,c))
elif choice=='/':
    c=a/b
    print("{}/{}={}".format(a,b,c))
elif choice=='%':
    c=a%b
    print("{}%{}={}".format(a,b,c))
elif choice=='**':
    c=a**b
    print("{}**{}={}".format(a,b,c))
elif choice=='//':
    c=a//b
    print("{}//{}={}".format(a,b,c))
else:
    print("enter valid choice!!!!!!!")