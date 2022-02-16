class car:
    def __init__(self,yr,mk,s):
        self.__year_model = yr
        self.__make = mk 
        self.__speed = s
    
    def set_year(self,yr):
        self.__year_model = yr 
    
    def set_make(self,mk):
        self.__make = mk 

    def accelerate(self,s):
        self.__speed += 5 
    
    def brake(self,s):
        self.__speed -= 5 
    
    def get_year_model(self,yr):
        return self.__year_model
    
    def get_make(self,mk):
        return self._make 
    
    def get_speed(self,s):
        return self.__speed
    


