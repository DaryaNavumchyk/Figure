from figure import Figure
import math


class Circle(Figure):
      
    def __init__(self, radius):  
        self.radius=radius

    def _getRadius(self):
        return self.radius
                    
    def getSquare(self):
        return self.radius * math.pi
  
    def getPerimeter(self):
        return self.radius * math.pi * 2



