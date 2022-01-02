from figure import Figure

class Triagle:
    
    def __init__(self, height, side1, side2, side3):
       self.height=height             
       self.side1=side1
       self.side2=side2
       self.side3=side3
              
    def _getheight1(self):        
        return self.height

    def _getside1(self):     
        return self.side1
    
    def _getside2(self):   
        return self.side2
        
    def _getside3(self):   
        return self.side3
            
    def getSquare(self):
        return self.height*self.side1*0.5
    
    def getPerimeter(self):
        return self.side1+self.side2+self.side3