print('''1:Area of triangle
2:Area of rectangle
3:Area of square''')
choice=input("enter your choice::")
if choice=='1':
    b=int(input("enter the base::"))
    h=int(input("enter the height"))
    triangle=lambda b,h:(b*h)/2
    print("Area of triangle::",triangle(b,h))

if choice=='2':
    l=int(input("enter the length::"))
    w=int(input("enter the width::"))
    rectangle=lambda l,w:l*w
    print("Area of rectangle::",rectangle(l,w))
    
if choice=='3':
    a=int(input("enter the side::"))
    square=lambda a:a**2
    print("Area of square::",square(a))
