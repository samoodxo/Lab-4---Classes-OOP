PI = 3.14
class Circle:
    def __init__(self,radius) -> None:
        self.radius = radius
    def display_area(self):
        return PI * self.radius
    def display_perimeter(self):
        return (2*PI) * self.radius
    
#Create Objects Example

C1 = Circle(25)
print(C1.display_area())
print(C1.display_perimeter())