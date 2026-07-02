import math

class circle:
    def __init__(self,radius):
       self.radius=radius
    
    def perimeter(self):
        return 2*math.pi*self.radius
        

    def area(self):
        return math.pi*(self.radius**2)
        
   
    
radius=int(input("Enter radius of the cirle:"))
mycircle=circle(radius)
print("Area of circle:",mycircle.area())
print("Perimeter of cirle",mycircle.perimeter())

   