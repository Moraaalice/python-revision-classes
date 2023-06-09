#Define a Circle class allowing to create a circleC (O, r) with center O(a, b) and radius r using the constructor:
#Define a Area() method of the class which calculates the area of ​​the circle.
#Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.
#Define a testBelongs() method of the class which allows to test whether a point A(x, y) belongs to the 
# circle C(O, r) or not.
class Circle:
    def __init__(self,center,radius):
        self.center = center
        self.radius = radius
    
    def area(self):
        PI = 3.14
        return  PI * self.radius * self.radius 
    
    def perimetere(self):
        PI = 3.14
        return 2*PI *self.radius 
    
    def test_belongs(self,pointX,pointY):
        import math
        distance = math.sqrt(pointX**2 + pointY**2)
        return distance
    
        
        

