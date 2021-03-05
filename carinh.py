#inheritce for car as parent and model as child class

class car:
    def c_display(self):     
        print("TATA")
class model(car):       
    def m_display(self):
        print("NEXON")
        
obj=model()
print("car model:",end=" ")
obj.m_display()
print("car company:",end=" ")
obj.c_display()