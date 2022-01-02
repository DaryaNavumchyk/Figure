from figure import Figure

class Square:
    
    def __init__(self, side):
       self.side=side
              
    def _getRadius(self):        
        return self.side
            
    def getSquare(self):
        return self.side**2
    
    def getPerimeter(self):
        return self.side*2
    
    
