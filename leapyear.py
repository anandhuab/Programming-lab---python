i=int(input("Enter the year::"))
if i%4==0 and i%100!=0:
    print("{} is leap Year".format(i))
elif i%400==0:
    print("{} is leap Year".format(i))
else:
    print("{} is not a leap year".format(i))
