#Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
#Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the
# area of ​​the rectangle.
#Create a method display() that displays the length, width, perimeter and area of an object created using an 
# instantiation on rectangle class.
#Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and 
# another Volume() method to calculate the volume of the Parallelepiped.
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def perimeter(self):
        return self.length *2 + self.width * 2
    
    def area(self):
        return self.length * self.width
    
    def display(self):
        print("area:",self.area())
        print("perimetre:",self.perimeter())
        print("length:",self.length)
        print("width:",self.width)  
        
#This is class inheritance       
class Parallepipede(Rectangle):
    def __init__(self, length, width,height):
        super().__init__(length, width)
        self.height = height
       
    def volume(self):
        return self.length * self.width * self.height
          
          
