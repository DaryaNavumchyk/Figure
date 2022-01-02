from figure import Figure

class Rectangle(Figure):
    
    def __init__(self, width, height):
       self.width=width
       self.height=height
       
    def _getWidth(self):        
        return self.width
     
    def _getHeight(self):        
        return self.height
       
    def getSquare(self):
        return self.width * self.height
    
    def getPerimeter(self):
        return self.width + self.height
    
    
    
    
    