#lst=[-1,-2,-3,1,2,3]
number=int(input("Enter Total number of elements in list : "))
lst=[]
for i in range(number):
    value=int(input("Enter a number :"))
    lst.append(value)  

print("possitive nuumbers in list::")
for i in range(len(lst)):
    if lst[i]>0:
        print(lst[i],end=" ")
