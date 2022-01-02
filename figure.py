from abc import ABC, abstractmethod
 
 
class Figure(ABC):
                  
    @abstractmethod
    def getSquare(self):
        pass 
    
    @abstractmethod
    def getPerimeter(self):
        pass
        
        
        
