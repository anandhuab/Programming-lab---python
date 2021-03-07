class rectangle:
    def __init__(self,l,b):
        self.__length=l
        self.__width=b
    def __lt__(self,other):
        
        first_rect=self.__length*self.__width
        second_rect=other.__length*other.__width
        return first_rect<second_rect
r1=rectangle(5,6)
r2=rectangle(7,8)
print(r1<r2)
