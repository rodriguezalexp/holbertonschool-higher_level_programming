#!/usr/bin/python3                                                                                                                            
"""part of base geometry function                                                                                                             
                                                                                                                                              
"""                                                                                                                                           
                                                                                                                                              
                                                                                                                                              
class BaseGeometry:                                                                                                                           
    def area(self):                                                                                                                           
        """[summary]                                                                                                                          
                                                                                                                                              
        Raises:                                                                                                                               
            Exception: exeption to check is area is not implement                                                                             
        """                                                                                                                                   
        raise Exception("area() is not implemented")                                                                                          
                                                                                                                                              
    def integer_validator(self, name, value):                                                                                                 
        """                                                                                                                                                                                                  
        """                                                                                                                                   
                                                                                                                                              
        if type(value) is not int:                                                                                                            
            raise TypeError("{:s} must be an integer".format(name))                                                                             
        if value <= 0 or value < 0:                                                                                                           
            raise ValueError("{:s} must be greater than 0".format(name))
           
if __name__ == "__main__":                                                                                                                    
    import doctest                                                                                                                            
    doctest.testfile('tests/7-base_geometry.txt')
